import numpy as np
import pandas as pd
import sklearn.preprocessing

import config


class Scale:

    def __init__(self):
        """

        """

        self.scaler = sklearn.preprocessing.StandardScaler(with_mean=False)
        
        self.numeric = config.Config().numeric

    def exc(self, blob: pd.DataFrame) -> np.ndarray:
        """

        :param blob:
        :return:
        """

        # The numeric fields
        fields_numeric_ = list(set(self.numeric).intersection(set(blob.columns)))

        # The categorical fields
        fields_categorical_ = list(set(blob.columns).difference(set(self.numeric)))

        # Scaling the numeric fields only
        scaled_ = self.scaler.fit_transform(X=blob[fields_numeric_].values)

        return np.concatenate((scaled_, blob[fields_categorical_].values), axis=1)
