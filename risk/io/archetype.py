import collections
import os

import numpy as np
import pandas as pd

import config


class Archetype:

    def __init__(self):
        """

        """

        self.configurations = config.Config()

        properties = self.properties()
        self.fields = properties.fields

    def __get(self, url) -> pd.DataFrame:

        try:
            data = pd.read_csv(filepath_or_buffer=url, sep=' ', header=None, encoding='utf-8')
        except OSError as err:
            raise Exception(err.strerror) in err

        data.columns = self.fields

        return data

    def __write(self, data: pd.DataFrame, filename: str) -> bool:
        
        try:
            data.to_csv(path_or_buf=os.path.join(self.configurations.data, filename),
                        header=True, index=False, encoding='utf-8')
            return True
        except OSError as err:
            raise Exception(err)

    @staticmethod
    def properties():

        ArchetypeProperties = collections.namedtuple(
            typename='ArchetypeProperties', field_names=['fields', 'target', 'tcf'])

        # Fields
        fields = ['e_chq_acc_status', 'duration_months', 'credit_history', 'purpose',
                  'credit_amount', 'savings_acc_class', 'curr_emp_class', 'i_rate_by_disp_inc',
                  'sex_and_status', 'other_debtors_class', 'curr_res_since', 'property',
                  'age_years', 'other_i_plans', 'housing', 'n_e_credits_this_bank', 'job',
                  'n_dependants', 'telephone', 'foreign_worker', 'acceptable']

        # The field of target labels
        target = 'acceptable'

        # TCF: Textual Categorical Fields
        tcf = {
            'fields': ['e_chq_acc_status', 'credit_history', 'purpose', 'savings_acc_class',
                       'curr_emp_class', 'sex_and_status', 'other_debtors_class', 'property',
                       'other_i_plans', 'housing', 'job', 'telephone', 'foreign_worker'],
            'arrays': [np.array(['A11', 'A12', 'A13', 'A14']), np.array(['A30', 'A31', 'A32', 'A33', 'A34']),
                       np.array(['A40', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47', 'A48', 'A49', 'A410']),
                       np.array(['A61', 'A62', 'A63', 'A64', 'A65']), np.array(['A71', 'A72', 'A73', 'A74', 'A75']),
                       np.array(['A91', 'A92', 'A93', 'A94', 'A95']), np.array(['A101', 'A102', 'A103']),
                       np.array(['A121', 'A122', 'A123', 'A124']), np.array(['A141', 'A142', 'A143']),
                       np.array(['A151', 'A152', 'A153']), np.array(['A171', 'A172', 'A173', 'A174']),
                       np.array(['A191', 'A192']), np.array(['A202', 'A201'])]
        }

        return ArchetypeProperties._make((fields, target, tcf))
        
    def exc(self, url: str, filename: str) -> pd.DataFrame:
        
        data = self.__get(url=url)
        if self.__write(data=data, filename=filename):
            return data
