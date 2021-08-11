import json
import logging
import os

import numpy as np
import pandas as pd

import config
import risk.embedding.representations


class Interface:

    def __init__(self, training: pd.DataFrame, properties: dict):
        """

        :param training:
        :param properties:
        """

        self.training = training
        self.properties = properties

        # Config
        self.configurations = config.Config()
        self.path = os.path.join(self.configurations.warehouse, 'data', 'modelling', 'representations')

        # Logging
        logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.logger = logging.getLogger(__name__)

    def __restructure(self, embedded, mappings) -> pd.DataFrame:
        
        numeric = self.training[self.properties['numeric']]
        binary = self.training[self.properties['binary']]
        target = self.training[self.properties['target']]
        polytomous = self.training[list(mappings.keys())]

        return pd.concat((numeric, embedded, binary, target, polytomous),
                         axis=1, ignore_index=False)
        
    @staticmethod
    def __decompose(representations) -> (pd.DataFrame, dict):

        # The embedded forms of the polytomous categorical fields
        frames = [representations[i][0] for i in np.arange(len(representations))]
        embedded = pd.concat(frames, axis=1, ignore_index=False)

        # The 'polytomous categorical fields' & 'T SNE Representation' mappings
        mappings = {representations[i][2]: representations[i][1] for i in np.arange(len(representations))}
        
        return embedded, mappings

    def __write(self, data: pd.DataFrame):

        try:
            data.to_csv(path_or_buf=os.path.join(self.path, 'data.csv'),
                        header=True, index=False, encoding='utf-8')
            return True
        except OSError as err:
            raise Exception(err.strerror)

    def exc(self):

        # Embeddings, and the associated mappings
        groups = self.properties['polytomous']
        representations = risk.embedding.representations.Representations(blob=self.training).\
            exc(groups=groups)
        embedded, mappings = self.__decompose(representations=representations)

        # Next, include the DataFrame of embeddings in the training data set
        data = self.__restructure(embedded=embedded, mappings=mappings)

        # Write
        if self.__write(data=data):

            with open(os.path.join(self.path, 'mappings.json'), 'w') as disk:
                json.dump(mappings, disk)

            self.logger.info(data.info())
