import pandas as pd
import numpy as np
import collections


class Representations:

    def __init__(self):
        """
        Constructor
        """

        self.binary_fields = ['A192', 'A201', 'female']

    @staticmethod
    def attributes():

        InstancesAttributes = collections.namedtuple(
            typename='InstancesAttributes', field_names=['url', 'dtype', 'target'])

        url = 'https://raw.githubusercontent.com/exhypotheses/risk/develop/warehouse/representations/data.csv'

        dtype = {'duration_months': np.int64, 'credit_amount': np.int64, 'i_rate_by_disp_inc': np.int64,
                 'curr_res_since': np.int64, 'age_years': np.int64, 'n_e_credits_this_bank': np.int64,
                 'n_dependants': np.int64,
                 'e_chq_acc_status_1': np.float64, 'e_chq_acc_status_2': np.float64,
                 'credit_history_1': np.float64, 'credit_history_2': np.float64,
                 'purpose_1': np.float64, 'purpose_2': np.float64,
                 'savings_acc_class_1': np.float64, 'savings_acc_class_2': np.float64,
                 'curr_emp_class_1': np.float64, 'curr_emp_class_2': np.float64,
                 'sex_and_status_1': np.float64, 'sex_and_status_2': np.float64,
                 'other_debtors_class_1': np.float64, 'other_debtors_class_2': np.float64,
                 'property_1': np.float64, 'property_2': np.float64,
                 'other_i_plans_1': np.float64, 'other_i_plans_2': np.float64,
                 'housing_1': np.float64, 'housing_2': np.float64,
                 'job_1': np.float64, 'job_2': np.float64,
                 'A192': np.uint8, 'A201': np.uint8, 'female': np.uint8, 'reasonable': np.uint8}

        target = 'reasonable'

        return InstancesAttributes._make((url, dtype, target))

    def data(self):

        attributes = self.attributes()

        try:
            data_ = pd.read_csv(filepath_or_buffer=attributes.url, header=0,
                                encoding='utf-8', dtype=attributes.dtype)
        except OSError as err:
            raise Exception(err.strerror) in err

        return data_
