import pandas as pd
import collections

import sklearn.model_selection


class Split:
    
    def __init__(self, splitting: collections.namedtuple):
        """

        :param splitting: A collection of named parameters, and their values, for
                         the sklearn.model_selection.train_test_split() function
        """

        self.splitting = splitting

    def exc(self, data: pd.DataFrame, labels: pd.Series) -> (pd.DataFrame, pd.DataFrame, pd.Series, pd.Series):
        """

        :param data:
        :param labels:
        :return:
        """

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
            data, labels,
            test_size=self.splitting.test_size,
            random_state=self.splitting.random_state,
            stratify=labels)

        return x_train, x_test, y_train, y_test
