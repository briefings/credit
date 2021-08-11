import logging
import os
import sys
import requests
import json

import pandas as pd


def main():

    risk.io.definitions.Definitions().exc()

    # Initial Steps
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data'
    risk.steps.initial.Initial(url=url).exc()

    # Embedding
    risk.steps.embedding.Embedding().exc()

    # Premodelling
    sampled, scaler = risk.steps.premodelling.Premodelling().exc()
    logger.info('\n %s', sampled.info())
    logger.info('\n %s', scaler)


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
    import risk.io.definitions

    import risk.steps.initial
    import risk.steps.embedding
    import risk.steps.premodelling

    # Config
    configurations = config.Config()

    main()
