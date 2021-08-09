import os
import pandas as pd
import collections

import sklearn.model_selection

import config


class Split:

    def __init__(self, arguments: collections.namedtuple('SplittingArguments',
                                                         ['train_size', 'random_state', 'target', 'strata'])):
        """

        :param arguments: A collection of named arguments, and their values, for
                         the sklearn.model_selection.train_test_split() function
        """

        self.arguments = arguments

        self.configurations = config.Config()
        self.path = os.path.join(self.configurations.warehouse, 'splits', 'scikit')

    def __write(self, training: pd.DataFrame, testing: pd.DataFrame):
        """

        :param training:
        :param testing:
        :return:
        """

        training.to_csv(path_or_buf=os.path.join(self.path, 'training.csv'),
                        header=True, index=False, encoding='UTF-8')
        testing.to_csv(path_or_buf=os.path.join(self.path, 'testing.csv'),
                       header=True, index=False, encoding='UTF-8')

    def exc(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data:
        :return:
        """

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
            data.drop(columns=self.arguments.target),
            data[self.arguments.target],
            train_size=self.arguments.train_size,
            random_state=self.arguments.random_state,
            stratify=data[self.arguments.strata])

        training = pd.concat((x_train.reset_index(drop=True), y_train.reset_index(drop=True)), axis=1,
                             ignore_index=False)
        testing = pd.concat((x_test.reset_index(drop=True), y_test.reset_index(drop=True)), axis=1,
                            ignore_index=False)
        
        self.__write(training=training, testing=testing)

        return training
