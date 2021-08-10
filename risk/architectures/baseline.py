import yaml
import json
import os

import config


class Baseline:
    
    def __init__(self):
        """
        
        """

        self.configurations = config.Config()
        self.path = os.path.join(self.configurations.warehouse, 'data', 'baseline')

    def __properties(self) -> dict:
        """

        :return:
        """

        properties = {
            'target': ['acceptable'],
            'numeric': self.configurations.numeric,
            'categoricalFields': ['e_chq_acc_status', 'credit_history', 'purpose', 'savings_acc_class',
                                  'curr_emp_class', 'sex_and_status', 'other_debtors_class', 'property',
                                  'other_i_plans', 'housing', 'job', 'telephone', 'foreign_worker', 'female'],
            'binary': [],
            'polytomous': {}
        }

        with open(os.path.join(self.path, 'properties.json'), 'w') as disk:
            json.dump(properties, disk)

        return properties

    def __arguments(self) -> dict:

        arguments = {
            'url': 'https://raw.githubusercontent.com/exhypotheses/risk/develop/warehouse/data/baseline/data.csv',
            'basename': 'data.csv',
            'properties': 'https://raw.githubusercontent.com/exhypotheses/risk/develop/warehouse/data/baseline/properties.json',
            'definitions': 'https://raw.githubusercontent.com/exhypotheses/risk/develop/data/definitions.json',
            'fields': ['duration_months', 'credit_amount', 'i_rate_by_disp_inc', 'curr_res_since', 'age_years',
                       'n_e_credits_this_bank', 'n_dependants', 'e_chq_acc_status', 'credit_history', 'purpose',
                       'savings_acc_class', 'curr_emp_class', 'sex_and_status', 'other_debtors_class', 'property',
                       'other_i_plans', 'housing', 'job', 'telephone', 'foreign_worker', 'female', 'acceptable'],
            'types': ['int64', 'int64', 'int64', 'int64', 'int64', 'int64', 'int64', 'str', 'str', 'str', 'str',
                      'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'int8', 'int8']}

        try:
            with open(os.path.join(self.path, 'arguments.yml'), 'w') as disk:
                yaml.dump(arguments, disk)
        except yaml.YAMLError as err:
            raise Exception(err)

        return arguments

    def exc(self):

        properties = self.__properties()
        arguments = self.__arguments()

        return properties, arguments
