import os


# noinspection PyUnresolvedReferences,PyProtectedMember
class Config:

    def __init__(self):
        """
        Constructor

        self.root = os.path.abspath(__package__)
        """

        # Seed
        self.SEED = 5

        # Numeric fields
        self.numeric = ['duration_months', 'credit_amount', 'i_rate_by_disp_inc', 'curr_res_since', 'age_years',
                        'n_e_credits_this_bank', 'n_dependants']

        # Target field
        self.target = 'acceptable'

        # Paths
        self.warehouse = os.path.join(os.getcwd(), 'warehouse')
        self.data = os.path.join(os.getcwd(), 'data')
