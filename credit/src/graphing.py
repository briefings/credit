import pandas as pd
import numpy as np
import collections

class Graphing:

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def attributes():

        InstancesAttributes = collections.namedtuple(
            typename='InstancesAttributes', field_names=['url', 'dtype', 'labels'])

        url = 'https://raw.githubusercontent.com/briefings/credit/develop/warehouse/data/graphing.csv'

        dtype = {'duration_months': np.int64, 'credit_amount': np.int64, 'i_rate_by_disp_inc': np.int64,
                 'curr_res_since': np.int64, 'age_years': np.int64, 'n_e_credits_this_bank': np.int64,
                 'n_dependants': np.int64, 'e_chq_acc_status': np.int64, 'credit_history': np.int64,
                 'purpose': np.int64, 'savings_acc_class': np.int64, 'curr_emp_class': np.int64,
                 'sex_and_status': np.int64, 'other_debtors_class': np.int64, 'property': np.int64,
                 'other_i_plans': np.int64, 'housing': np.int64, 'job': np.int64, 'telephone': np.int64,
                 'foreign_worker': np.int64, 'sex': np.int64, 'reasonable': np.int64}

        labels = 'reasonable'

        return InstancesAttributes._make((url, dtype, labels))

    def data(self):

        attributes = self.attributes()

        try:
            data_ = pd.read_csv(filepath_or_buffer=attributes.url, header=0,
                               encoding='utf-8', dtype=attributes.dtype)
        except OSError as err:
            raise Exception(err.strerror) in err

        return data_
