import numpy as np
import pandas as pd
import sklearn.preprocessing

import config


class Scalers:

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

    def apply(self, blob: pd.DataFrame, scaler: sklearn.preprocessing.StandardScaler) -> pd.DataFrame:
        """
        Use scaler to scale the numerical data, subsequently reconstruct the data

        :param blob:
        :param scaler:
        :return:
        """

        # Fields
        numerical, categorical = self.fields(blob=blob.copy())

        # Scaling numerical fields
        scaled_: np.ndarray = scaler.transform(X=blob[numerical])
        unscaled = blob[categorical]

        # Altogether
        numeric = pd.DataFrame(data=scaled_, columns=numerical)
        bits = pd.DataFrame(data=unscaled, columns=categorical)
        frame = pd.concat((numeric, bits), axis=1, ignore_index=False)

        return frame

    def determine(self, blob: pd.DataFrame) -> sklearn.preprocessing.StandardScaler:
        """

        :return:
        """

        numerical, _ = self.fields(blob=blob.copy())

        # Scaling the numeric fields only
        scaler = sklearn.preprocessing.StandardScaler(with_mean=True)
        scaler.fit(X=blob[numerical].values)

        return scaler
