import numpy as np
import collections


# noinspection PyUnresolvedReferences,PyProtectedMember
class Credit:

    def __init__(self):
        """
        The URL of the original, which does not have a header:
            http://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29
        """

    @staticmethod
    def attributes():
        """

        :return:
        """

        InstancesAttributes = collections.namedtuple(
            typename='InstancesAttributes', field_names=['url', 'labels'])

        url = 'https://raw.githubusercontent.com/briefings/credit/develop/data/credit.csv'

        labels = ['label']

        return InstancesAttributes._make((url, labels))

    @staticmethod
    def categories():
        """
        For 'dictionary' refer to README

        :return:
        """

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

        dictionary = {}

        return CategoricalData._make((fields, arrays, dictionary))
