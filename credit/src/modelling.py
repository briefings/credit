import pandas as pd

import config


class Modelling:

    def __init__(self):

        configurations = config.Config()

        self.modelling = configurations.modelling()

    def read_(self):

        try:
            data = pd.read_csv(filepath_or_buffer=self.modelling.url, header=0,
                               encoding='utf-8', dtype=self.modelling.dtype)
        except OSError as err:
            raise Exception(err.strerror) in err

        return data

    def exc(self):

        data = self.read_()

        return data
