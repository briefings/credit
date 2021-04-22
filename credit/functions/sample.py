import sklearn.utils

import collections

import numpy as np


class Sample:

    def __init__(self, sampling: collections.namedtuple):
        """

        :param sampling: A collection of named parameters, and their values, for
                         the sklearn.utils.resample() function
        """

        self.sampling = sampling

    def sample(self, indices: np.ndarray, labels: np.ndarray) -> np.ndarray:
        """

        :param indices:
        :param labels:
        :return:
        """

        negative = indices[labels != 1]
        positive = indices[labels == 1]

        j = sklearn.utils.resample(
            negative, replace=True, n_samples=self.sampling.n_samples, random_state=self.sampling.random_state)
        k = sklearn.utils.resample(
            positive, replace=True, n_samples=self.sampling.n_samples, random_state=self.sampling.random_state)

        return sklearn.utils.shuffle(np.concatenate((j, k)))

    def exc(self, features: np.ndarray, labels: np.ndarray) -> (np.ndarray, np.ndarray):
        """

        :param features:
        :param labels:
        :return:
        """

        indices = np.arange(labels.shape[0])

        index = self.sample(indices=indices, labels=labels)

        return features[index, :], labels[index]
