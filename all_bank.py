import warnings
from logging import warning
import pandas as pd
import numpy as np
import csv, time
import pyproj
from pandas.io.json import json_normalize
import os
import webbrowser
import folium
from folium import plugins
print(folium.__version__)
import re
import googlemaps
import webbrowser
import plotly.express as px

df = pd.read_csv('2021_ALL_BNK_STOR_BASE_change.csv', encoding='UTF-8',usecols=['가로위치좌표', '세로위치좌표'])

df['가로위치좌표'] = pd.to_numeric(df['가로위치좌표'], errors="coerce")
df['세로위치좌표'] = pd.to_numeric(df['세로위치좌표'], errors="coerce")


# my_key = "AIzaSyAPA6edshMP0QnrmGKdyHeWhdbGv9id4yM"
# maps = googlemaps.Client(key=my_key)  # my_key값 입력



# with open('2021_ALL_BNK_STOR_BASE_change.csv', encoding='cp949',usecols=['가로위치좌표','세로위치좌표']) as csv_file:
#     csv_data = csv.reader(csv_file)
#     print(csv_data)
#     for data in csv_data:
#         for d in data:
#             print(d, end ='\t')
#         print()

# df = pd.read_csv('2021_ALL_BNK_STOR_BASE_change.csv', encoding='UTF-8',usecols=['가로위치좌표', '세로위치좌표'])

# df['가로위치좌표'] = pd.to_numeric(df['가로위치좌표'], errors="coerce")
# df['세로위치좌표'] = pd.to_numeric(df['세로위치좌표'], errors="coerce")

# df = df.dropna()
# df.index=range(len(df))
# df.tail()

# # 좌표계 변환 함수
# def project_array(coord, p1_type, p2_type):
#     """
#     좌표계 변환 함수
#     - coord: x, y 좌표 정보가 담긴 NumPy Array
#     - p1_type: 입력 좌표계 정보 ex) epsg:5179
#     - p2_type: 출력 좌표계 정보 ex) epsg:4326
#     """
#     p1 = pyproj.Proj(init=p1_type)
#     p2 = pyproj.Proj(init=p2_type)
#     fx, fy = pyproj.transform(p1, p2, coord[:, 0], coord[:, 1])
#     return np.dstack([fx, fy])[0]

# coord = np.array(df)
# coord

# # 좌표계 정보 설정
# p1_type = "epsg:2097"
# p2_type = "epsg:4326"

# # project_array() 함수 실행
# result = project_array(coord, p1_type, p2_type)
# result

# print(result)

# df['경도'] = result[:, 0]
# df['위도'] = result[:, 1]

# df.tail()

# # 데이터 100개 랜덤 추출
# sample = df.sample(n=100)

# # 지도 중심 좌표 설정
# lat_c, lon_c = 37.53165351203043, 126.9974246490573

# # Folium 지도 객체 생성
# m = folium.Map(location=[lat_c, lon_c], zoom_start=6, tiles = 'cartodbpositron')

# geo_json ='https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
# # 마커 생성
# for _, row in sample.iterrows():
#     lat, lon = row['위도'], row['경도']
#     folium.Marker(location=[lat, lon]).add_to(m)

# folium.Choropleth(
#     geo_data = geo_json,
#     name = 'choropleth',
#     data = df,
#     columns=['위도','경도'],
#     key_on='feature.properties.name',
#     fill_color = 'YlGn',
#     fill_opacity = 0.7,
#     line_opacity = 1,
#     legend_name = 'Population (people)'
# ).add_to(m)

# m