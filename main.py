import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

from request_data_extractor import get_rows_and_headers

data_url = "http://derivativefind.icicidirect.com/find20/Derivatives/FNOFundFlow/CompanyOptionTrends?symbol=NIFTY&optionType=CE"

response = requests.get(data_url)

soup = BeautifulSoup(response.content, 'html5lib')
target_script_tag = soup.find('script', text=re.compile(r'datastr'))

data_dict, data_headers = get_rows_and_headers(target_script_tag.text)

data_rows = []
for row in data_dict['rows']:
    data_rows.append(row['cell'])

data_df = pd.DataFrame(data_rows, columns=data_headers)

print()
