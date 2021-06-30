import imblearn
import pandas as pd

import config


class Sample:

    def __init__(self):
        """
        Constructor
        """

        configurations = config.Config()
        self.SEED = configurations.SEED

    def exc(self, blob: pd.DataFrame, pivot: list):
        """

        :param blob: The data set that will be sampled
        :param pivot: The list of fields about which sampling should occur
        :return:
        """

        # Over-sampling via SVNSMOTE
        # https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SVMSMOTE.html
        svnsmote = imblearn.over_sampling.SVMSMOTE(random_state=self.SEED, sampling_strategy='all', k_neighbors=9)
        x_training_resampled, y_pivot_resampled = svnsmote.fit_resample(X=blob.drop(columns=pivot), y=blob[pivot])

        return pd.concat((x_training_resampled, y_pivot_resampled), axis=1, ignore_index=False)