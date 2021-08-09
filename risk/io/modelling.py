import os

import numpy as np
import pandas as pd
import sklearn.preprocessing

import config

import risk.io.archetype


class Modelling:

    def __init__(self, frame: pd.DataFrame):
        """

        :param frame:
        """

        self.frame = frame

        archetype = risk.io.archetype.Archetype()
        self.properties = archetype.properties()

        self.configurations = config.Config()
        self.path = os.path.join(self.configurations.warehouse, 'data', 'modelling')

    def __bits(self):
        """

        :return:
        """

        # One Hot Encoding
        # noinspection PyUnresolvedReferences
        enc = sklearn.preprocessing.OneHotEncoder(
            categories=self.properties.tcf['arrays'], drop='if_binary', sparse=False, dtype=np.int)
        bits_ = enc.fit_transform(X=self.frame.copy()[self.properties.tcf['fields']])
        columns = [column[(column.rindex('_') + 1):] for column in enc.get_feature_names()]
        bits = pd.DataFrame(data=bits_, columns=columns)

        # 'if binary' drops the original names.  This statements reverses the change.
        bits.rename(columns={'A192': 'telephone', 'A201': 'foreign_worker'}, inplace=True)

        return bits

    def __write(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        try:
            data.to_csv(path_or_buf=os.path.join(self.path, 'data.csv'),
                        header=True, index=False, encoding='utf-8')
            return True
        except OSError as err:
            raise Exception(err.strerror)

    def exc(self):

        bits = self.__bits()
        left = self.frame.drop(columns=self.properties.tcf['fields'])
        data = pd.concat((bits, left), axis=1, ignore_index=False)

        if self.__write(data=data):
            return data
