# %%
from param import Parameterized, Dict
import pickle
#%%

class HUD(Parameterized):
    fy_report = "https://ntmpsweb.dc3n.navy.mil/FLTMPS/Personnel/Course%20Grads/PersAddFYTrngRqmtsReport.aspx"


    def make_url(self):
    url = '
    json = {
    'TYPE': 'D',
    'UIC': '000000',
    'UICTitle': 'MY UIC PROFILE',
    'GRP': 'UIC',
    'PageSize': '250'
}