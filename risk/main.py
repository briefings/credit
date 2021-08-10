import logging
import os
import sys
import collections


def main():

    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data'

    # The original data
    data = risk.io.archetype.Archetype(). \
        exc(url=url, filename='risk.csv')
    logger.info(data.info())

    # Address inconsistencies
    baseline = risk.io.baseline.Baseline(frame=data).exc()
    risk.architectures.baseline.Baseline().exc()
    logger.info(baseline.info())

    # Prepare for modelling: Textual Categorical Fields > One Hot Encodings OR Binary
    modelling = risk.io.modelling.Modelling(frame=baseline).exc()
    properties, _ = risk.architectures.modelling.Modelling().exc()
    logger.info(modelling.info())

    # Split into training/testing sets
    SplittingArguments = collections.namedtuple(
        typename='SplittingArguments', field_names=['train_size', 'random_state', 'target', 'strata'])
    training = risk.functions.split.Split(arguments=SplittingArguments._make(
        (0.65, configurations.SEED, configurations.target, ['female', configurations.target]))).exc(data=modelling)
    logger.info(training.info())

    # Get embeddings
    dataframe = risk.embeddings.interface.Interface(
        training=training, properties=properties).exc()
    logger.info(dataframe.info())

    # Model


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'risk'))

    # Logging
    logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Classes
    import config

    import risk.io.archetype
    import risk.io.baseline
    import risk.io.definitions
    import risk.io.modelling
    import risk.architectures.baseline
    import risk.architectures.modelling

    import risk.functions.split
    import risk.embeddings.interface

    # Instantiating
    risk.io.definitions.Definitions().exc()

    configurations = config.Config()

    main()
