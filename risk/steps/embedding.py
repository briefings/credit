import os
import json

import pandas as pd

import config
import risk.embeddings.interface


class Embedding:

    def __init__(self):
        """

        """

        self.configurations = config.Config()
        self.source = os.path.join(self.configurations.warehouse, 'data', 'modelling')

    def __training(self):

        try:
            data = pd.read_csv(
                filepath_or_buffer=os.path.join(self.source, 'splits', 'scikit', 'training.csv'),
                header=0, encoding='utf-8')
        except OSError as err:
            raise Exception(err.strerror)

        return data

    def __properties(self):

        try:
            with open(os.path.join(self.source, 'properties.json'), 'r') as disk:
                literal = json.load(disk)
        except OSError as err:
            raise Exception(err)

        return literal

    def exc(self):

        training = self.__training()
        properties = self.__properties()

        # Apply T-SNE Embedding to polytomous categorical fields
        risk.embeddings.interface.Interface(
            training=training, properties=properties).exc()