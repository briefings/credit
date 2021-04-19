import collections
import os

import numpy as np


# noinspection PyUnresolvedReferences,PyProtectedMember
class Config:

    def __init__(self):
        self.root = os.path.abspath(__package__)

    @staticmethod
    def source():
        SourceAttributes = collections.namedtuple(
            typename='SourceAttributes',
            field_names=['url', 'dtype', 'numeric', 'label'])

        url = 'https://raw.githubusercontent.com/briefings/credit/develop/data/credit.csv'

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

        numeric = ['duration_months', 'credit_amount', 'i_rate_by_disp_inc', 'curr_res_since', 'age_years',
                   'n_e_credits_this_bank', 'n_dependants']

        label = ['healthy']

        return SourceAttributes._make((url, dtype, numeric, label))

    @staticmethod
    def constraints():
        FieldConstraints = collections.namedtuple(typename='FieldConstraints',
                                                  field_names=['minimal', 'additional', 'selections'])

        return FieldConstraints._make(
            (['sex', 'A91', 'A92', 'A93', 'A94', 'age_years'],
             ['A61', 'A62', 'A63', 'A64', 'A65', 'A71', 'A72', 'A73', 'A74', 'A75',
              'curr_res_since', 'n_e_credits_this_bank', 'A171', 'A172', 'A173', 'A174'],
             ['curr_res_since', 'A171', 'A172', 'A173', 'A174']))

    @staticmethod
    def categories():
        CategoricalData = collections.namedtuple(
            typename='CategoricalData', field_names=['fields', 'arrays', 'dictionary'])

        fields = ['e_chq_acc_status', 'credit_history', 'purpose', 'savings_acc_class',
                  'curr_emp_class', 'sex_and_status', 'other_debtors_class', 'property',
                  'other_i_plans', 'housing', 'job', 'telephone', 'foreign_worker']

        arrays = [np.array(['A11', 'A12', 'A13', 'A14']), np.array(['A30', 'A31', 'A32', 'A33', 'A34']),
                  np.array(['A40', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47', 'A48', 'A49', 'A410']),
                  np.array(['A61', 'A62', 'A63', 'A64', 'A65']), np.array(['A71', 'A72', 'A73', 'A74', 'A75']),
                  np.array(['A91', 'A92', 'A93', 'A94', 'A95']), np.array(['A101', 'A102', 'A103']),
                  np.array(['A121', 'A122', 'A123', 'A124']), np.array(['A141', 'A142', 'A143']),
                  np.array(['A151', 'A152', 'A153']), np.array(['A171', 'A172', 'A173', 'A174']),
                  np.array(['A191', 'A192']), np.array(['A201', 'A202'])]

        dictionary = {'e_chq_acc_status': {'A11': 0, 'A12': 1, 'A13': 2, 'A14': 3},
                      'credit_history': {'A30': 0, 'A31': 1, 'A32': 2, 'A33': 3, 'A34': 4},
                      'purpose': {'A40': 0, 'A41': 1, 'A42': 2, 'A43': 3, 'A44': 4, 'A45': 5, 'A46': 6, 'A47': 7,
                                  'A48': 8, 'A49': 9, 'A410': 10},
                      'savings_acc_class': {'A61': 0, 'A62': 1, 'A63': 2, 'A64': 3, 'A65': 4},
                      'curr_emp_class': {'A71': 0, 'A72': 1, 'A73': 2, 'A74': 3, 'A75': 4},
                      'sex_and_status': {'A91': 0, 'A92': 1, 'A93': 2, 'A94': 3, 'A95': 4},
                      'other_debtors_class': {'A101': 0, 'A102': 1, 'A103': 2},
                      'property': {'A121': 0, 'A122': 1, 'A123': 2, 'A124': 3},
                      'other_i_plans': {'A141': 0, 'A142': 1, 'A143': 2},
                      'housing': {'A151': 0, 'A152': 1, 'A153': 2},
                      'job': {'A171': 0, 'A172': 1, 'A173': 2, 'A174': 3},
                      'telephone': {'A191': 0, 'A192': 1},
                      'foreign_worker': {'A201': 1, 'A202': 0}}

        return CategoricalData._make((fields, arrays, dictionary))
