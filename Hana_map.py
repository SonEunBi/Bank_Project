import requests
import json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import os
import webbrowser
import folium
from folium import plugins
print(folium.__version__)
import re

file = r'C:\Users\treac\OneDrive\바탕 화면\인턴\데이터(종합)\하나은행\2021_ALL_BNK_STOR_BASE_change.csv'
file = file.replace('\\','//')

df = pd.read_csv(file, encoding='cp949') 
print(df.head(5))
m = folium.Map(
    location = [37.566345, 126.977893],
    tiles = 'cartodbpositron'
)
geo_json ='https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'


folium.Choropleth(
    geo_data = geo_json,
    name = 'choropleth',
    data = df,
    columns=['기준년월','전체점포일련번호'],
    key_on='feature.properties.name',
    fill_color = 'YlGn',
    fill_opacity = 0.7,
    line_opacity = 1,
    legend_name = 'Population (people)'
).add_to(m)
m