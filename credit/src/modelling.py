import pandas as pd

import config


class Baseline:

    def __init__(self):

        configurations = config.Config()

        self.instances = configurations.instances()

    def read_(self):

        try:
            data = pd.read_csv(filepath_or_buffer=self.instances.url, header=0,
                               encoding='utf-8', dtype=self.instances.dtype)
        except OSError as err:
            raise Exception(err.strerror) in err

        return data

    def exc(self):

        data = self.read_()

        return data
