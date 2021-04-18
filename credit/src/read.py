import pandas as pd

import config


class Read:

    def __init__(self):

        configurations = config.Config()

        self.source = configurations.source()

    def read_(self):

        try:
            data = pd.read_csv(filepath_or_buffer=self.source.url, header=0,
                               encoding='utf-8', dtype=self.source.dtype)
        except OSError as err:
            raise Exception(err.strerror) in err

        return data

    def exc(self):

        data = self.read_()

        return data
