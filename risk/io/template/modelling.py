import config
import os
import json
import yaml


class Modelling:

    def __init__(self):

        self.configurations = config.Config()
        self.path = os.path.join(self.configurations.warehouse, 'data', 'modelling')

    def __properties(self):
        """

        :return:
        """

        properties = {
            'target': ['acceptable'],
            'numeric': self.configurations.numeric,
            'categoricalFields': ['e_chq_acc_status', 'credit_history', 'purpose', 'savings_acc_class',
                                  'curr_emp_class', 'sex_and_status', 'other_debtors_class', 'property',
                                  'other_i_plans', 'housing', 'job', 'telephone', 'foreign_worker', 'female'],
            'binary': ['telephone', 'foreign_worker', 'female'],
            'polytomous': {'e_chq_acc_status': ['A11', 'A12', 'A13', 'A14'],
                           'credit_history': ['A30', 'A31', 'A32', 'A33', 'A34'],
                           'purpose': ['A40', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47', 'A48', 'A49', 'A410'],
                           'savings_acc_class': ['A61', 'A62', 'A63', 'A64', 'A65'],
                           'curr_emp_class': ['A71', 'A72', 'A73', 'A74', 'A75'],
                           'sex_and_status': ['A91', 'A92', 'A93', 'A94', 'A95'],
                           'other_debtors_class': ['A101', 'A102', 'A103'],
                           'property': ['A121', 'A122', 'A123', 'A124'],
                           'other_i_plans': ['A141', 'A142', 'A143'],
                           'housing': ['A151', 'A152', 'A153'], 'job': ['A171', 'A172', 'A173', 'A174']}
        }

        with open(os.path.join(self.path, 'properties.json'), 'w') as disk:
            json.dump(properties, disk)

    def __arguments(self):
        """

        :return:
        """

        items = {'A11': 'int8', 'A12': 'int8', 'A13': 'int8', 'A14': 'int8',
                 'A30': 'int8', 'A31': 'int8', 'A32': 'int8', 'A33': 'int8', 'A34': 'int8',
                 'A40': 'int8', 'A41': 'int8', 'A42': 'int8', 'A43': 'int8', 'A44': 'int8',
                 'A45': 'int8', 'A46': 'int8', 'A47': 'int8', 'A48': 'int8', 'A49': 'int8', 'A410': 'int8',
                 'A61': 'int8', 'A62': 'int8', 'A63': 'int8', 'A64': 'int8', 'A65': 'int8',
                 'A71': 'int8', 'A72': 'int8', 'A73': 'int8', 'A74': 'int8', 'A75': 'int8',
                 'A91': 'int8', 'A92': 'int8', 'A93': 'int8', 'A94': 'int8', 'A95': 'int8',
                 'A101': 'int8', 'A102': 'int8', 'A103': 'int8',
                 'A121': 'int8', 'A122': 'int8', 'A123': 'int8', 'A124': 'int8',
                 'A141': 'int8', 'A142': 'int8', 'A143': 'int8',
                 'A151': 'int8', 'A152': 'int8', 'A153': 'int8',
                 'A171': 'int8', 'A172': 'int8', 'A173': 'int8', 'A174': 'int8',
                 'telephone': 'int8', 'foreign_worker': 'int8', 'duration_months': 'int64',
                 'credit_amount': 'int64', 'i_rate_by_disp_inc': 'int64', 'curr_res_since': 'int64',
                 'age_years': 'int64', 'n_e_credits_this_bank': 'int64', 'n_dependants': 'int64',
                 'female': 'int8', 'acceptable': 'int8'}

        arguments = {
            'url': "https://raw.githubusercontent.com/exhypotheses/risk/develop/warehouse/data/modelling/data.csv",
            'basename': 'data.csv',
            'properties': 'https://raw.githubusercontent.com/exhypotheses/risk/develop/warehouse/data/modelling/properties.json',
            'definitions': 'https://raw.githubusercontent.com/exhypotheses/risk/develop/data/definitions.json',
            'fields': list(items.keys()),
            'types': list(items.values())}

        try:
            with open(os.path.join(self.path, 'arguments.yml'), 'w') as disk:
                yaml.dump(arguments, disk)
        except yaml.YAMLError as err:
            raise Exception(err)

    def exc(self):

        self.__properties()
        self.__arguments()
