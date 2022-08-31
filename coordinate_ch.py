import pandas as pd
import numpy as np
import pyproj
import folium

df = pd.read_csv("./2021_ALL_BNK_STOR_BASE_change.csv",
                 encoding='cp949',
                 usecols=['좌표정보(x)','좌표정보(y)'])