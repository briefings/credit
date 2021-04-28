import collections

import numpy as np
import pandas as pd
import sklearn.utils


class Sample:

    def __init__(self, frame: pd.DataFrame, strata: list, sampling: collections.namedtuple):
        """

        :param frame:
        :param strata: The field/s of frame that will guide the sampling
        :param sampling: Wherein
                            sampling.n_samples: the number of instances per distinct strata values combination
                            sampling.random_state: ...
        """

        self.frame = frame
        self.strata = strata
        self.sampling = sampling

    def sample(self, vector: np.ndarray) -> pd.DataFrame:
        """

        :param vector:
        :return:
        """

        indices = sklearn.utils.shuffle(vector)

        rebuilt = self.frame.iloc[indices, :]
        rebuilt.reset_index(drop=True, inplace=True)

        return rebuilt

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        permutations = self.frame[self.strata].to_numpy()
        combinations = np.unique(permutations, axis=0)

        vector = np.array([])
        for combination in combinations:
            states = (permutations == combination)
            conditions = np.all(states, axis=1)

            indices = self.frame[conditions].index
            array_ = indices.to_numpy()

            select = sklearn.utils.resample(
                array_, replace=True, n_samples=self.sampling.n_samples, random_state=self.sampling.random_state)

            vector = np.concatenate((vector, select))

        return self.sample(vector=vector)
