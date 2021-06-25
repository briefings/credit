import pandas as pd
import numpy as np


class Reference:

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def __mappings(feature: str, patterns: pd.DataFrame) -> pd.DataFrame:
        """

        :param feature:
        :param patterns:
        :return:
        """

        # The instances whereby feature is True/1
        case = patterns.loc[patterns[feature] == 1, :]

        # Hence
        if case.empty:
            mappings = pd.DataFrame()
        else:
            # The estimated embeddings values for the feature in question
            mappings = case.groupby(by=list(case.columns.drop(labels=feature))).count()

        return mappings

    @staticmethod
    def __mode(feature: str, mappings) -> np.ndarray:
        """

        :param feature:
        :param mappings:
        :return:
        """

        # The mode will be used as a feature's mapping
        frame = mappings.reset_index()
        mode_index = frame[feature].idxmax()
        frame = frame.copy().iloc[mode_index:(mode_index + 1), :]
        frame.loc[mode_index, feature] = 1

        mode = frame[['tsne_1', 'tsne_2']].values[0]

        return mode

    def exc(self, features: list, patterns: pd.DataFrame) -> dict:
        """

        :param features:
        :param patterns: a data frame that consists of the one hot encoding features/fields of a category & the
                                   corresponding T-SNE 1 & 2 fields
        :return:
        """

        # Determine the embeddings per feature
        dictionary = {}
        for feature in features:

            mappings = self.__mappings(feature=feature, patterns=patterns)
            if mappings.empty:
                continue
            else:
                mode = self.__mode(feature=feature, mappings=mappings)
                dictionary.__setitem__(feature, list(mode))

        return dictionary
