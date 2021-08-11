import logging
import os

import pandas as pd
import pymc3
import sklearn.preprocessing
import theano

import config
import risk.functions.dag
import risk.modelling.assets
import risk.modelling.model


class Modelling:

    def __init__(self):
        """

        """

        logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.logger = logging.getLogger(__name__)

        self.configurations = config.Config()
        self.path = os.path.join(self.configurations.warehouse, 'model')

        self.x_training_fields = ['duration_months', 'credit_amount', 'e_chq_acc_status_1', 'e_chq_acc_status_2',
                                  'credit_history_1', 'credit_history_2', 'purpose_1', 'purpose_2',
                                  'savings_acc_class_1', 'savings_acc_class_2', 'housing_1', 'housing_2']

    def __dag(self, lm):

        dag = risk.functions.dag.DAG()
        dag.exc(model=lm, directory=self.path)

    # noinspection PyUnresolvedReferences
    def __assets(self, lm: pymc3.model.Model, trace: pymc3.backends.base.MultiTrace,
                 xshared: theano.tensor, scaler: sklearn.preprocessing.StandardScaler):

        pocket = {
            'lm': lm,
            'ndraws': trace.report.n_draws,
            'nchains': trace.nchains,
            'xshared': xshared,
            'target': self.configurations.target,
            'regressors': ','.join(self.x_training_fields),
            'scaler': scaler
        }

        assets = risk.modelling.assets.Assets(directory=self.path)
        assets.pocket_(pocket=pocket)
        assets.trace_(trace=trace)

    def exc(self, sampled: pd.DataFrame, scaler):
        """


        :param sampled:
        :param scaler:
        :return:
        """

        lm, trace, xshared = risk.modelling.model.Model().exc(
            sampled=sampled, x_training_fields=self.x_training_fields)

        self.__assets(lm=lm, trace=trace, xshared=xshared, scaler=scaler)
        self.__dag(lm=lm)
        self.logger.info('\n %s', type(lm))
