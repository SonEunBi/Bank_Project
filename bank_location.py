from cProfile import label
import warnings
from logging import warning
import pandas as pd
import numpy as np
import sys
import os
labels = pd.read_csv('../data/all_bank.csv', encoding='cp949')
# print(labels) 

list_name= ['시도코드', '은행명', '주소']
list_p=[]
list_path=[]

labels.drop(columns=['지점구분', '관할지점', '영업구분', '개점일', '전화번호'], inplace=True)
labels.dropna(inplace=True)
pd.set_option('display.max_rows', None)

code_location = labels[['시도코드']]
name_city = labels[['시군구명']]
name_city1 = labels[['동명']]
name_bank = labels[['은행명']]
print(code_location, name_city, name_bank, sep='\,')

sys.stdout = open('all_bank.txt', 'w')

sys.stdout.close()

labels.to_csv()
# print(labels.dtypes) #데이터타입 확인
# print(labels.isnull().sum())
# labels.rename(columns={""})