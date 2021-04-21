import numpy as np
import pandas as pd
import sklearn.preprocessing

import config


class Scale:

    def __init__(self):
        """

        """

        self.numeric = config.Config().numeric

    def exc(self, blob: pd.DataFrame) -> (np.ndarray, sklearn.preprocessing.StandardScaler):
        """

        :param blob:
        :return:
        """

        # The numeric & categorical fields
        numerical = list(set(self.numeric).intersection(set(blob.columns)))
        categorical = list(set(blob.columns).difference(set(self.numeric)))

        # Scaling the numeric fields only
        scaler = sklearn.preprocessing.StandardScaler(with_mean=False)
        scaler.fit(X=blob[numerical].values)
        scaled_ = scaler.transform(X=blob[numerical].values)

        # Altogether
        data = np.concatenate((scaled_, blob[categorical].values), axis=1)

        return data, scaler
