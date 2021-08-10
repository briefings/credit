import logging
import os
import sys


def main():

    # Initial Steps
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data'
    risk.steps.initial.Initial(url=url).exc()

    # Model
    #   - scale
    #   - sample
    #   - bayesian logistic regression


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'risk'))

    # Logging
    logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Classes
    import risk.steps.initial

    main()
