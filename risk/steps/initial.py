import collections
import logging

import config
import risk.architectures.baseline
import risk.architectures.modelling
import risk.embeddings.interface
import risk.functions.split
import risk.io.archetype
import risk.io.baseline
import risk.io.definitions
import risk.io.modelling


class Initial:

    def __init__(self, url):
        """

        :param url:
        """

        # URL of original data set
        self.url = url

        # Logging
        logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.logger = logging.getLogger(__name__)

        # Instantiating
        risk.io.definitions.Definitions().exc()

        # Config
        self.configurations = config.Config()

    def exc(self):

        # The original data
        data = risk.io.archetype.Archetype(). \
            exc(url=self.url, filename='risk.csv')
        self.logger.info(data.info())

        # Address inconsistencies
        baseline = risk.io.baseline.Baseline(frame=data).exc()
        risk.architectures.baseline.Baseline().exc()
        self.logger.info(baseline.info())

        # Prepare for modelling: Textual Categorical Fields > One Hot Encodings OR Binary
        modelling = risk.io.modelling.Modelling(frame=baseline).exc()
        risk.architectures.modelling.Modelling().exc()
        self.logger.info(modelling.info())

        # Split into training/testing sets
        SplittingArguments = collections.namedtuple(
            typename='SplittingArguments', field_names=['train_size', 'random_state', 'target', 'strata'])
        arguments = SplittingArguments._make(
            (0.65, self.configurations.SEED, self.configurations.target, ['female', self.configurations.target]))

        risk.functions.split.Split(arguments=arguments).exc(data=modelling)
