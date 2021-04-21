import sklearn.utils

import collections

import numpy as np
import pandas as pd


class Sample:

    def __init__(self, sampling: collections.namedtuple):
        """

        :param sampling: A collection of named parameters, and their values, for
                         the sklearn.utils.resample() function
        """

        self.sampling = sampling

    def sample(self, indices: np.ndarray, true: np.ndarray) -> np.ndarray:
        """

        :param indices:
        :param true:
        :return:
        """

        negative = indices[true != 1]
        positive = indices[true == 1]

        j = sklearn.utils.resample(
            negative, replace=True, n_samples=self.sampling.n_samples, random_state=self.sampling.random_state)
        k = sklearn.utils.resample(
            positive, replace=True, n_samples=self.sampling.n_samples, random_state=self.sampling.random_state)

        return sklearn.utils.shuffle(np.concatenate((j, k)))

    def exc(self, x_train: pd.DataFrame, y_train: pd.Series) -> (pd.DataFrame, pd.Series):
        """

        :param x_train:
        :param y_train:
        :return:
        """

        indices = np.arange(y_train.shape[0])
        true = y_train.values.flatten()

        index = self.sample(indices=indices, true=true)

        x_train = x_train.iloc[index, :]
        y_train = y_train.iloc[index]

        return x_train, y_train
