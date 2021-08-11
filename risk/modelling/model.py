import logging

import numpy as np
import pandas as pd
import pymc3
import theano

import config


class Model:

    def __init__(self):
        """

        """

        self.configurations = config.Config()

        logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.logger = logging.getLogger(__name__)

    # noinspection PyUnresolvedReferences
    @staticmethod
    def __model(xshared: theano.tensor, y_training_: np.ndarray, x_training_fields: list) \
            -> (pymc3.model.Model, pymc3.backends.base.MultiTrace):

        with pymc3.Model() as lm:

            pymc3.glm.GLM(x=xshared, y=y_training_, intercept=True, labels=x_training_fields,
                          priors={'Regressor': pymc3.StudentT.dist(nu=5.0, mu=0, sigma=15.0)},
                          family=pymc3.families.Binomial())

            # Trace
            trace = pymc3.sample(tune=1000, draws=2000)

        return lm, trace

    def exc(self, sampled: pd.DataFrame, x_training_fields: list):
        """

        :param sampled:
        :param x_training_fields:
        :return:
        """

        # Input
        x_training_ = sampled[x_training_fields].to_numpy()
        xshared = theano.shared(x_training_)

        # Output
        y_training_ = sampled[self.configurations.target].to_numpy()

        # Model
        lm, trace = self.__model(xshared=xshared, y_training_=y_training_,
                                 x_training_fields=x_training_fields)

        return lm, trace, xshared
