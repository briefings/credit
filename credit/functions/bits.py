import pandas as pd

import credit.src.archetype


class Bits:

    def __init__(self):
        """
        An example of a dictionary of variates, including variate name; note that each
        variate IS a dictionary ->

            self.categories.dictionary = {
                'e_chq_acc_status': {'A11': 0, 'A12': 1, 'A13': 2, 'A14': 3},
                'credit_history': {'A30': 0, 'A31': 1, 'A32': 2, 'A33': 3, 'A34': 4},
                'purpose': {'A40': 0, 'A41': 1, 'A42': 2, 'A43': 3, 'A44': 4,
                            'A45': 5, 'A46': 6, 'A47': 7, 'A48': 8, 'A49': 9,
                            'A410': 10},
                ...
            }
        """

        cr = credit.src.archetype.Credit()
        self.categories = cr.categories()

    @staticmethod
    def encode(points: pd.Series, variates: dict):
        """

        :param points:
        :param variates:
        :return:
        """

        # For renaming
        rename = {v: k for k, v in variates.items()}

        # Create a new series wherein a category will be represented by its number, rather than text, code
        numerical = points.apply(lambda x: variates[x])

        # One-Hot-Encoding via get_dummies
        encoded = pd.get_dummies(data=numerical)

        # Name fields
        encoded.rename(columns=rename, inplace=True)

        return encoded

    def exc(self, data: pd.DataFrame):
        """

        :param data:
        :return:
        """

        bits = pd.DataFrame()

        for key, value in self.categories.dictionary.items():
            frame = self.encode(points=data[key], variates=value)
            bits = pd.concat([bits, frame], axis=1)

        return bits
