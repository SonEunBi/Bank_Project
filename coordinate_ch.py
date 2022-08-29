import pandas as pd
import numpy as np
import pyproj
import folium

df = pd.read_csv("./sample/fulldata_07_24_04_P_일반음식점.csv",
                 encoding='cp949',
                 usecols=['좌표정보(x)','좌표정보(y)'])