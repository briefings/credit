import collections

import numpy as np
import pandas as pd


class Baseline:

    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def attributes():
        """

        :return:
        """

        InstancesAttributes = collections.namedtuple(
            typename='InstancesAttributes', field_names=['url', 'dtype', 'labels'])

        url = 'https://raw.githubusercontent.com/exhypotheses/risk/develop/warehouse/data/baseline.csv'

        dtype = {'duration_months': np.int64, 'credit_amount': np.int64, 'i_rate_by_disp_inc': np.int64,
                 'curr_res_since': np.int64, 'age_years': np.int64, 'n_e_credits_this_bank': np.int64,
                 'n_dependants': np.int64, 'e_chq_acc_status': str, 'credit_history': str, 'purpose': str,
                 'savings_acc_class': str, 'curr_emp_class': str, 'sex_and_status': str, 'other_debtors_class': str,
                 'property': str, 'other_i_plans': str, 'housing': str, 'job': str, 'telephone': str, 'foreign_worker': str,
                 'female': np.int64, 'reasonable': np.int64}

        labels = 'reasonable'

        return InstancesAttributes._make((url, dtype, labels))

    def data(self):
        """

        :return:
        """

        attributes = self.attributes()

        try:
            data_ = pd.read_csv(filepath_or_buffer=attributes.url, header=0,
                                encoding='utf-8', dtype=attributes.dtype)
        except OSError as err:
            raise Exception(err.strerror) in err

        return data_
