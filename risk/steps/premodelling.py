import os
import json
import pandas as pd
import sklearn.preprocessing

import config

import risk.functions.scale
import risk.functions.sample


class Premodelling:

    def __init__(self):
        """

        """

        self.configurations = config.Config()
        self.source = os.path.join(self.configurations.warehouse, 'data', 'modelling')

    def __representations(self) -> pd.DataFrame:

        try:
            data = pd.read_csv(filepath_or_buffer=os.path.join(self.source, 'representations', 'data.csv'),
                               header=0, encoding='utf-8')
        except OSError as err:
            raise Exception(err.strerror)

        return data

    def __mapped(self) -> list:

        try:
            with open(os.path.join(self.source, 'representations', 'mappings.json'), 'r') as disk:
                mappings: dict = json.load(disk)
        except OSError as err:
            raise Exception(err)

        return list(mappings.keys())

    def __scale(self, training) -> (pd.DataFrame, sklearn.preprocessing.StandardScaler):

        scale = risk.functions.scale.Scale()
        scaler = scale.exc(blob=training.drop(columns=self.configurations.target))
        left = scale.apply(blob=training.drop(columns=self.configurations.target), scaler=scaler)
        scaled = pd.concat((left, training[self.configurations.target]), axis=1, ignore_index=False)

        return scaled, scaler

    def __sample(self, scaled) -> pd.DataFrame:

        sample = risk.functions.sample.Sample()
        sampled = sample.exc(blob=scaled, target=self.configurations.target)

        return sampled

    def exc(self):

        data = self.__representations()
        mapped = self.__mapped()

        training = data.drop(columns=mapped)
        scaled, scaler = self.__scale(training=training)
        sampled = self.__sample(scaled=scaled)

        return sampled, scaler
