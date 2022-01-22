import pandas as pd
import os
path1 = '/Users/mato/Desktop/奶粉/好评'
path2 = '/Users/mato/Desktop/奶粉/差评'
path1_list = os.listdir(path1)
path1_list.sort(key=lambda x: int(x.split('.')[0]))
path1_list = os.listdir(path1)
path1_list.sort(key=lambda x: int(x.split('.')[0]))

path1 = '/Users/mato/Desktop/奶粉/好评结果/'
path2 = '/Users/mato/Desktop/奶粉/差评结果'
word_data = pd.DataFrame()
word_data.to_excel(path1 + '111.xlsx')
