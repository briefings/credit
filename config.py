import os


# noinspection PyUnresolvedReferences,PyProtectedMember
class Config:

    def __init__(self):
        """

        """

        self.root = os.path.abspath(__package__)

        self.numeric = ['duration_months', 'credit_amount', 'i_rate_by_disp_inc', 'curr_res_since', 'age_years',
                        'n_e_credits_this_bank', 'n_dependants']
