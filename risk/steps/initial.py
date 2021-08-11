import collections
import logging

import config
import risk.architectures.baseline
import risk.architectures.modelling
import risk.embedding.interface
import risk.functions.split
import risk.io.archetype
import risk.io.baseline

import risk.io.modelling


class Initial:

    def __init__(self, url):
        """

        :param url:
        """

        # URL of original data set
        self.url = url

        # Config
        self.configurations = config.Config()

        # Logging
        logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.logger = logging.getLogger(__name__)

    def __archetype(self):

        # The original data
        data = risk.io.archetype.Archetype(). \
            exc(url=self.url, filename='risk.csv')

        return data

    @staticmethod
    def __baseline(data):

        # Address inconsistencies
        baseline = risk.io.baseline.Baseline(frame=data).exc()
        risk.architectures.baseline.Baseline().exc()

        return baseline

    @staticmethod
    def __modelling(baseline):

        # Prepare for modelling: Textual Categorical Fields > One Hot Encodings OR Binary
        modelling = risk.io.modelling.Modelling(frame=baseline).exc()
        risk.architectures.modelling.Modelling().exc()

        return modelling

    def __split(self, modelling):

        # Split into training/testing sets
        SplittingArguments = collections.namedtuple(
            typename='SplittingArguments', field_names=['train_size', 'random_state', 'target', 'strata'])
        arguments = SplittingArguments._make(
            (0.65, self.configurations.SEED, self.configurations.target, ['female', self.configurations.target]))

        training, _ = risk.functions.split.Split(arguments=arguments).exc(data=modelling)

        return training

    def exc(self):

        data = self.__archetype()
        self.logger.info(data.info())

        baseline = self.__baseline(data=data)
        self.logger.info(baseline.info())

        modelling = self.__modelling(baseline=baseline)
        self.logger.info(modelling.info())

        training = self.__split(modelling=modelling)
        self.logger.info(training.info())
