import pandas as pd
import numpy as np


class Bijections:
    """
    Remaps features & embeddings w.r.t. bijective set-up
    """

    def __init__(self, reference: dict, key: str):
        """
        Each 'key' denotes a categorical variable, and the ...

        :param reference:
        :param key:
        """

        self.reference = reference
        self.key = key
        self.members = list(reference.keys())

    @staticmethod
    def biject(series: pd.Series, reference: dict) -> pd.Series:
        """

        :param series:
        :param reference:
        :return:
        """

        return series.apply(lambda x: np.array(reference[x]))

    def __melt(self, blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        data = blob.copy().melt(value_vars=self.members, var_name=self.key, value_name='true', ignore_index=False)
        data = data.loc[data['true'] == 1, :]
        data.drop(columns=['true'], inplace=True)

        return data

    def __transform(self, blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        # Set-up
        data = blob.copy()
        key = self.key

        # Bijections
        bijections = self.biject(series=data[key], reference=self.reference)

        # Assign
        data.loc[:, ['{}_1'.format(key), '{}_2'.format(key)]] = np.vstack(bijections.values)

        return data[['{}_1'.format(key), '{}_2'.format(key)]]

    def exc(self, blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        frame = self.__melt(blob=blob)
        frame = self.__transform(blob=frame)

        return frame
