import logging
import os
import sys
import collections


def main():

    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data'

    data = risk.io.archetype.Archetype(). \
        exc(url=url, filename='risk.csv')
    logger.info(data.info())

    baseline = risk.io.baseline.Baseline(frame=data).exc()
    risk.io.template.baseline.Baseline().exc()
    logger.info(baseline.info())

    modelling = risk.io.modelling.Modelling(frame=baseline).exc()
    risk.io.template.modelling.Modelling().exc()
    logger.info(modelling.info())

    SplittingArguments = collections.namedtuple(
        typename='SplittingArguments', field_names=['train_size', 'random_state', 'target', 'strata'])
    training = risk.functions.split.Split(arguments=SplittingArguments._make(
        (0.65, configurations.SEED, configurations.target, ['female', configurations.target]))).exc(data=modelling)
    logger.info(training.info())


if __name__ == '__main__':

    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'risk'))

    logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    import config

    import risk.io.archetype
    import risk.io.baseline
    import risk.io.definitions
    import risk.io.modelling

    import risk.io.template.baseline
    import risk.io.template.modelling

    import risk.functions.split

    risk.io.definitions.Definitions().exc()

    configurations = config.Config()

    main()
