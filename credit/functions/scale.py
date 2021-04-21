import numpy as np
import pandas as pd
import sklearn.preprocessing

import config


class Scale:

    def __init__(self, blob: pd.DataFrame):
        """

        """

        self.blob = blob

        # From config.py
        self.numeric = config.Config().numeric

        # The numeric & categorical fields
        self.numerical = list(set(self.numeric).intersection(set(blob.columns)))
        self.categorical = list(set(blob.columns).difference(set(self.numeric)))

    def assemble(self, scaler) -> np.ndarray:
        """

        :param scaler:
        :return:
        """

        # Scale
        scaled_ = scaler.transform(X=self.blob[self.numerical].values)

        # Altogether
        return np.concatenate((scaled_, self.blob[self.categorical].values), axis=1)

    def exc(self) -> (np.ndarray, sklearn.preprocessing.StandardScaler):
        """

        :return:
        """

        # Scaling the numeric fields only
        scaler = sklearn.preprocessing.StandardScaler(with_mean=False)
        scaler.fit(X=self.blob[self.numerical].values)

        # Use scaler to scale the numerical data, subsequently reconstruct the data
        data = self.assemble(scaler=scaler)

        return data, scaler
