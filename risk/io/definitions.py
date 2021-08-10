import json
import os

import config


class Definitions:

    def __init__(self):
        """

        """

        self.configurations = config.Config()

    def exc(self):
        """

        :return:
        """

        definitions = {
            'e_chq_acc_status': {
                'desc': 'Existing Checking Account Status',
                'A11': '< 0DM',
                'A12': '[0 200)DM',
                'A13': '≥ 200DM',
                'A14': 'no checking account'},
            'credit_history': {
                'desc': 'Credit History',
                'A30': 'no credits taken,<br>all credits paid back duly',
                'A31': 'all credits at this<br>bank paid back duly',
                'A32': 'existing credits paid<br>back duly till now',
                'A33': 'delay in paying off in the past',
                'A34': 'critical account,<br>other credits existing elsewhere'},
            'purpose': {
                'desc': 'Purpose',
                'A40': 'car (new)',
                'A41': 'car (used)',
                'A42': 'furniture/equipment',
                'A43': 'radio/television',
                'A44': 'domestic appliances',
                'A45': 'repairs',
                'A46': 'education',
                'A47': 'probably vacation',
                'A48': 'retraining',
                'A49': 'business',
                'A410': 'others'},
            'savings_acc_class': {
                'desc': 'Savings Account/Bonds',
                'A61': '< 100DM',
                'A62': '[100 500)DM',
                'A63': '[500 1000)DM',
                'A64': '≥ 1000DM',
                'A65': 'unknown/no savings account'},
            'curr_emp_class': {
                'desc': 'Present Employment Since',
                'A71': 'unemployed',
                'A72': '< 1 year',
                'A73': '[1 4) years',
                'A74': '[4 7) years',
                'A75': '≥ 7 years'},
            'sex_and_status': {
                'desc': 'Personal Status & Sex',
                'A91': 'male: divorced/separated',
                'A92': 'female: divorced/separated/married',
                'A93': 'male: single',
                'A94': 'male: married/widowed',
                'A95': 'female: single'},
            'other_debtors_class': {
                'desc': 'Other Debtors/Guarantors',
                'A101': 'none',
                'A102': 'co-applicant',
                'A103': 'guarantor'},
            'property': {
                'desc': 'Property',
                'A121': 'real estate',
                'A122': 'b.s. savings agreement/life insurance',
                'A123': 'car or other, not in -- savings account/bond',
                'A124': 'unknown/no property'},
            'other_i_plans': {
                'desc': 'Other Installment Plans',
                'A141': 'bank',
                'A142': 'stores',
                'A143': 'none'},
            'housing': {
                'desc': 'Housing',
                'A151': 'rent',
                'A152': 'own',
                'A153': 'for free'},
            'job': {
                'desc': 'Job',
                'A171': 'unemployed/unskilled, non-resident',
                'A172': 'unskilled, resident',
                'A173': 'skilled employee/official',
                'A174': 'management/self-employed/HQE/officer'},
            'telephone': {
                'desc': 'Telephone',
                0: 'none',
                1: 'yes, registered'},
            'foreign_worker': {
                'desc': 'Foreign Worker',
                1: 'yes',
                0: 'no'},
            'female': {
                'desc': 'Sex',
                0: 'Male',
                1: 'Female'
            }
        }

        with open(os.path.join(self.configurations.data, 'definitions.json'), 'w') as disk:
            json.dump(definitions, disk)
