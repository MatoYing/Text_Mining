import pandas as pd
import numpy as np

"""
缺失值处理
重复值处理
异常值处理
字串符处理
"""

'''
数据缺失处理方法
1.删除缺失值
    删除记录：样本偏差
    删除属性：80%法则（这个属性80%的都缺失了）
2.缺失值填补
    均值；中位数；众数；特殊值（-1）
    前向后向填充（跟前面或后面数据一样）
    机器学习算法填补 
3.不处理
    用不到的属性
    算法可以接受缺失值
'''

####################################
# 删除缺失值

data = pd.read_excel('../data_pre-processing/data.xlsx')
# 批量获取每一列缺失值的情况
for column in data.columns:
    if column != '最近地铁距离':
        df = data[data[column].isnull()]  # 小型的内部判断过滤吧，不为true自动就删了
        print(column, '缺失值的个数为：', len(df), '缺失值的占比为：', len(df)/len(data))
    else:
        df = data[data[column] == '暂无数据']
        print(column, '缺失值的个数为：', len(df), '缺失值的占比为：', len(df) / len(data))

# 删除缺失值（行）
df1 = data.dropna()  # NaN
df2 = data[data['最近地铁距离'] != '暂无数据']
# 删除缺失值（列）
df3 = data.drop('整租/合租', axis=1)


####################################
# 缺失值填充

# 均值填充
df4 = data['房屋面积'].fillna(data['房屋面积'].mean())
print(df4.isnull())  # 为0
# 中位数填充
df5 = data['房屋面积'].fillna(data['房屋面积'].median())
# 众数填充(这里有问题，这个mode打印出来会有个类似index的东西（0    中楼层），所以不能直接fillna(data['楼层'].mode()))
print(data['楼层'].mode())
df6 = data['楼层'].fillna(data['楼层'].mode().values[0])
# 将特殊缺失值转化为缺失值
df7 = data['最近地铁距离'].replace('暂无数据', np.nan)
df7 = data['最近地铁距离'].fillna(data['最近地铁距离'].mean())
# 前向后向填充
df8 = data['最近地铁距离'].fillna(method='ffill')
df9 = data['最近地铁距离'].fillna(method='bfill', limit=1)  # limit意思就是只能向前填充1一个空值


"""
重复值处理
    删掉他
# """
# 查看重复值data[data.duplicated()]
df10 = data.drop_duplicates(keep='first')  # 保留重复值的第一个，last则代表保留重复值的最后一个
# 更高级：以某一列位重复值判依据进行删除
df11 = data.drop_duplicates(keep='first', subset='名称')



"""
异常值处理
    判别方法：物理判断（对客观事物已有的认识）；统计判断（给定置信概率和置信限）
    判别原则：
        散点图：点不在主要范围内
        （!）正态分布：距离平均值>3δ（P(|x-μ|>3δ) <= 0.003）
        不服从正态分布：距离平均值 VS n倍标准差
        (!)分位数判别：上分位 +1.5IQR、下分位 -1.5IQR（貌似与正太分布差不多）
        模型检测：聚类、回归
    处理方法：
        删除异常值
        视同缺失值，用可能值填补
        覆盖法（用上界或下界覆盖）
        不处理
"""

############################
# 三倍标准差判断 #
# 计算均值
price_mean = data['租价/月'].mean()
# 计算标准差
price_std = data['租价/月'].std()
# 定义超出均值的三倍标准差范围就是异常值
price_min = price_mean - 3 * price_std
price_max = price_mean + 3 * price_std
print(data[data['租价/月'].map(lambda x: (x > price_max) or (x < price_min))])
# 处理异常值（覆盖法）
ls1 =[]
for i in range(len(data)):
    x = data['租价/月'].iloc[i]
    if x < price_min:
        ls1.append(price_min)
    elif x > price_max:
        ls1.append(price_max)
    else:
        ls1.append(x)
data['三倍标准差（覆盖法）'] = ls1


# 四分位数判断 #
# 计算25分为
price_25 = data['租价/月'].quantile(0.25)  # 只有dataframe有
# 计算75分为
price_75 = data['租价/月'].quantile(0.75)
# 定义超出超出上分位和下分位的IQR（上分位-下分位）范围就是异常值
price_min = price_25 - 1.5 * (price_75 - price_25)
price_max = price_75 + 1.5 * (price_75 - price_25)
print(data[data['租价/月'].map(lambda x: (x > price_max) or (x < price_min))])
# 处理异常值，异常值变为缺失值
ls1 =[]
for i in range(len(data)):
    x = data['租价/月'].iloc[i]
    if x < price_min:
        ls1.append(np.nan)
    elif x > price_max:
        ls1.append(np.nan)
    else:
        ls1.append(x)
data['分位法'] = ls1
print(data[data['分位法'].notnull()])  # 可以通过这个直接删除
data['分位法'] = data['分位法'].fillna(data['分位法'].mean())
print(data[data['分位法'].isnull()])

"""
字符串处理
    字符串规整：
        大小写统一：capitalize()/upper()/lower()/title()
        空格处理：strip()
    字符串信息提取：
        字符替换：replace()
        字符切割：split()
"""
# 单独获取名称的小区信息
print(data['名称'].map(lambda x: x.split(' ')[0]))
# 批量获取卧室数
print(data['名称'].map(lambda x: float(x.split(' ')[1].split('室')[0])))