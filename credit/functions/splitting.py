import pandas as pd
import numpy as np

import collections

import sklearn.preprocessing

import config


class Splitting:
    """
    Class Structure

    Scaling is conducted **after splitting** in order to **avoid data leakage**;
    [more](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html)
    """

    def __init__(self, data: pd.DataFrame, drop: list, sampling: collections.namedtuple):
        """

        :param data: The data set in focus
        :param drop: The attributes, fields, that will be excluded from the model
        :param sampling:
        """

        self.data = data
        self.drop = drop
        self.sampling = sampling

        self.scaler = sklearn.preprocessing.StandardScaler(with_mean=False)

        configurations = config.Config()
        self.modelling = configurations.modelling()

    def points(self):
        """
        Retrieves the data readings & labels for the modelling exercise; questionable/inappropriate
        attributes are dropped.

        :return:
        """

        # Design Frame
        readings = self.data.drop(columns=self.drop).drop(columns=self.modelling.label)
        
        # Beware, this is a table
        labels = self.data[self.modelling.label]

        return readings, labels

    @staticmethod
    def split(readings, labels) -> (pd.DataFrame, pd.DataFrame, pd.Series, pd.Series):
        """

        :param readings:
        :param labels:
        :return:
        """

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
            readings, labels, test_size=0.4, random_state=5, stratify=labels)

        return x_train, x_test, y_train, y_test

    def sample(self, x_train, y_train) -> (pd.DataFrame, pd.Series):
        """

        :param x_train:
        :param y_train:
        :return:
        """

        indices = np.arange(y_train.shape[0])
        true = y_train.values.flatten()

        positive = indices[true == 1]
        negative = indices[true != 1]

        j = sklearn.utils.resample(
            negative, replace=True, n_samples=self.sampling.n_samples, random_state=self.sampling.random_state)
        k = sklearn.utils.resample(
            positive, replace=True, n_samples=self.sampling.n_samples, random_state=self.sampling.random_state)
        i = sklearn.utils.shuffle(np.concatenate((j, k)))

        x_train = x_train.iloc[i, :]
        y_train = y_train.iloc[i]

        return x_train, y_train

    def scale(self, blob) -> np.ndarray:
        """

        :param blob:
        :return:
        """

        fields_numeric_ = list(set(self.modelling.numeric).intersection(set(blob.columns)))
        fields_categorical_ = list(set(blob.columns).difference(set(self.modelling.numeric)))

        scaled_ = self.scaler.fit_transform(X=blob[fields_numeric_].values)

        return np.concatenate((scaled_, blob[fields_categorical_].values), axis=1)

    def exc(self) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
        """

        :return:
        """

        readings, labels = self.points()
        x_train, x_test, y_train, y_test = self.split(readings, labels)
        x_train, y_train = self.sample(x_train.copy(), y_train.copy())

        x_train = self.scale(x_train)
        x_test = self.scale(x_test)

        return x_train, x_test, y_train.values.flatten(), y_test.values.flatten()
