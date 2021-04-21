import numpy as np
import pandas as pd
import sklearn.preprocessing

import config


class Scale:

    def __init__(self):
        """
        Constructor
        """

        # From config.py
        self.numeric = config.Config().numeric

    def fields(self, blob: pd.DataFrame) -> (list, list):

        # The numeric & categorical fields
        numerical = list(set(self.numeric).intersection(set(blob.columns)))
        categorical = list(set(blob.columns).difference(set(self.numeric)))

        return numerical, categorical

    def apply(self, blob: pd.DataFrame, scaler: sklearn.preprocessing.StandardScaler) -> np.ndarray:
        """
        Use scaler to scale the numerical data, subsequently reconstruct the data

        :param blob:
        :param scaler:
        :return:
        """

        # Fields
        numerical, categorical = self.fields(blob=blob.copy())

        # Scaling numerical fields
        scaled_ = scaler.transform(X=blob[numerical].values)

        # Altogether
        return np.concatenate((scaled_, blob[categorical].values), axis=1)

    def determine(self, blob: pd.DataFrame) -> sklearn.preprocessing.StandardScaler:
        """

        :return:
        """

        numerical, _ = self.fields(blob=blob.copy())

        # Scaling the numeric fields only
        scaler = sklearn.preprocessing.StandardScaler(with_mean=False)
        scaler.fit(X=blob[numerical].values)

        return scaler
