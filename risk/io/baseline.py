import os

import pandas as pd

import config


class Baseline:

    def __init__(self, frame: pd.DataFrame):
        """

        :param frame:
        """

        self.frame = frame

        self.configurations = config.Config()
        self.path = os.path.join(self.configurations.warehouse, 'data', 'baseline')

    def __target(self) -> pd.DataFrame:
        """

        :return:
        """

        labels = self.frame[['acceptable']].copy()
        labels.loc[:, 'acceptable'] = labels['acceptable'].mod(2)

        return labels

    def __female(self) -> pd.DataFrame:
        """
        sex: 1 -> female, 0 -> male

        :return:
        """

        values: pd.Series = self.frame['sex_and_status'].copy().\
            apply(lambda x: 1 if (x == 'A92' or x == 'A95') else 0)
        values.rename('female', inplace=True)

        return values.to_frame()

    def __write(self, data: pd.DataFrame) -> bool:
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
        """

        :return:
        """

        female = self.__female()
        target = self.__target()

        data = pd.concat((self.frame.drop(columns='acceptable'), female, target), axis=1)

        if self.__write(data=data):
            return data
