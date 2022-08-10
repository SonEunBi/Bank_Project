import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions
import pandas as pd

url = 'https://golmok.seoul.go.kr/region/selectPopulation.json'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
data = soup.select('table')
table = data[0]

table_html = str(table)
table_df_list = pd.read_html(table_html)
table_df = table_df_list[0]
print(table_df)

# table_df_list = pd.find_all(url, header=0, encoding='utf-8')
# table_df = table_df_list[1:]
# print(table_df_list)
# table = parser_functions.make2d(data)

# df = pd.DataFrame(data=df[3], columns=df[3])
# df.to_csv('C:/bankTest/'+'table.csv', encoding='utf-8')