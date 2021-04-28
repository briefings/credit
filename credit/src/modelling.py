import pandas as pd
import numpy as np
import collections


# noinspection PyUnresolvedReferences,PyProtectedMember
class Modelling:

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def attributes():

        InstancesAttributes = collections.namedtuple(
            typename='InstancesAttributes', field_names=['url', 'dtype', 'labels', 'strata'])

        url = 'https://raw.githubusercontent.com/briefings/credit/develop/warehouse/data/modelling.csv'

        dtype = {'duration_months': np.int64, 'credit_amount': np.int64, 'i_rate_by_disp_inc': np.int64,
                 'curr_res_since': np.int64, 'age_years': np.int64, 'n_e_credits_this_bank': np.int64,
                 'n_dependants': np.int64, 'A11': np.uint8, 'A12': np.uint8, 'A13': np.uint8, 'A14': np.uint8,
                 'A30': np.uint8, 'A31': np.uint8, 'A32': np.uint8, 'A33': np.uint8, 'A34': np.uint8,
                 'A40': np.uint8, 'A41': np.uint8, 'A42': np.uint8, 'A43': np.uint8, 'A44': np.uint8,
                 'A45': np.uint8, 'A46': np.uint8, 'A48': np.uint8, 'A49': np.uint8, 'A410': np.uint8,
                 'A61': np.uint8, 'A62': np.uint8, 'A63': np.uint8, 'A64': np.uint8, 'A65': np.uint8,
                 'A71': np.uint8, 'A72': np.uint8, 'A73': np.uint8, 'A74': np.uint8, 'A75': np.uint8,
                 'A101': np.uint8, 'A102': np.uint8, 'A103': np.uint8, 'A121': np.uint8, 'A122': np.uint8,
                 'A123': np.uint8, 'A124': np.uint8, 'A141': np.uint8, 'A142': np.uint8, 'A143': np.uint8,
                 'A151': np.uint8, 'A152': np.uint8, 'A153': np.uint8, 'A171': np.uint8, 'A172': np.uint8,
                 'A173': np.uint8, 'A174': np.uint8, 'A191': np.uint8, 'A192': np.uint8, 'A202': np.uint8,
                 'A201': np.uint8, 'A91': np.uint8, 'A92': np.uint8, 'A93': np.uint8, 'A94': np.uint8,
                 'sex': np.int64, 'healthy': np.int64}

        labels = 'reasonable'

        strata = ['reasonable', 'sex']

        return InstancesAttributes._make((url, dtype, labels, strata))

    def data(self):

        attributes = self.attributes()

        try:
            data_ = pd.read_csv(filepath_or_buffer=attributes.url, header=0,
                               encoding='utf-8', dtype=attributes.dtype)
        except OSError as err:
            raise Exception(err.strerror) in err

        return data_
