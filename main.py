import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

from request_data_extractor import get_rows_and_headers


def get_data(script_name, option_type):
    data_url = 'http://derivativefind.icicidirect.com/find20/Derivatives/FNOFundFlow/CompanyOptionTrends?symbol='+script_name+'&optionType='+option_type

    response = requests.get(data_url)

    soup = BeautifulSoup(response.content, 'html5lib')
    target_script_tag = soup.find('script', text=re.compile(r'datastr'))

    data_dict, data_headers = get_rows_and_headers(target_script_tag.text)

    data_rows = []
    for row in data_dict['rows']:
        data_rows.append(row['cell'])

    data_df = pd.DataFrame(data_rows, columns=data_headers)
    return data_df


scripts_list = ['NIFTY', 'BANKNIFTY']

for script in scripts_list:
    ce_data = get_data(script, 'CE')
    pe_data = get_data(script, 'PE')
    ce_pe_data = ce_data.append(pe_data)
    print()

print()
