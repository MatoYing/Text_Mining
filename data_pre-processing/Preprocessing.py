import pandas as pd
import numpy as np

'''
数据预处理
1.标准化与归一化（由于各个评价指标的量级不同）
 （标准化：缩放到均值位0，方差位1）
 （归一化：缩放到0到1）
 （可以看到，经过归一化或者标准化，新图的数值的散点图和原图一样）
 （当原始数据不同维度特征的尺度(量纲)不一致时，需要标准化步骤对数据进行标准化或归一化处理，反之则不需要进行数据标准化。
  也不是所有的模型都需要做归一的，比如模型算法里面有没关于对距离的衡量，没有关于对变量间标准差的衡量。
  比如决策树，他采用算法里面没有涉及到任何和距离等有关的，所以在做决策树模型时，通常是不需要将变量做标准化的；
  另外，概率模型不需要归一化，因为它们不关心变量的值，而是关心变量的分布和变量之间的条件概率。）
 （如果你对处理后的数据范围有严格要求，那肯定是归一化，标准化是ML中更通用的手段，如果你无从下手，可以直接使用标准化；
  如果数据不为稳定，存在极端的最大最小值，不要用归一化。
  在分类、聚类算法中，需要使用距离来度量相似性的时候、或者使用PCA技术进行降维的时候，标准化表现更好；
  在不涉及距离度量、协方差计算的时候，可以使用归一化方法。）
2.数据离散化
  （分段离散化：比如说给一组年龄，多少到多少分为青年，中年）
  （等频离散化：就是先确定分几组，然后把年龄按顺序分成几组）
3.独热编码
  （就是例如青年、老年、中年，分别用100，010，001这样表示，就是将非数字转为数字）
4.数据映射
  （和独热编码差不多，这是把数字转为非数字）
'''

data = pd.read_excel('data.xlsx')
##
# 标准化
# #
data['房屋面积(标准化后)'] = (data['房屋面积'] - data['房屋面积'].mean()) / data['房屋面积'].std()  # std：标准差
# （查看下均值的情况）
print('均值(0)：', data['房屋面积(标准化后)'].mean(), sep='')
# （查看下标准差的情况）
print('标准差(1)：', data['房屋面积(标准化后)'].std(), sep='')

##
# 归一化
# #
data['房屋面积(归一化后)'] = (data['房屋面积'] - data['房屋面积'].min()) / (data['房屋面积'].max() - data['房屋面积'].min())
# 查看最小值
print('最小值(0)：', data['房屋面积(归一化后)'].min(), sep='')
# 查看最大值
print('最大值(1)：', data['房屋面积(归一化后)'].max(), sep='')

##
# 离散化
# #
# 等宽离散化 #
# 人为划分：对距离进行划分区间0-500为近，500-1000，1000-2000为远
bins = [0, 500, 1000, 2000]
data['等宽划分距离'] = pd.cut(data['最近地铁距离'], bins=bins)
# 查看每个划分区间多少值
print('每个划分区间多少值', data['等宽划分距离'].value_counts(), sep='')
# 等频离散化 #
data['等频划分距离'] = pd.qcut(data['最近地铁距离'], q=3)
print('每个划分区间多少值', data['等频划分距离'].value_counts(), sep='')

##
# 独热编码
# (解决了分类器不好处理属性数据的问题
# 在一定程度上也起到了扩充特征的作用)
# 0 1 0
# 1 0 0
# 0 0 1
# #
data['中楼层(独热编码)'] = pd.get_dummies(data['楼层'])['中楼层']
data['低楼层(独热编码)'] = pd.get_dummies(data['楼层'])['低楼层']
data['高楼层(独热编码)'] = pd.get_dummies(data['楼层'])['高楼层']

##
# 映射数据
# #
print('愿数据类型：', type(data['等宽划分距离'].iloc[0]), sep='')
data['等宽划分距离'] = data['等宽划分距离'].map(lambda x: str(x))
print('现数据类型：',type(data['等宽划分距离'].iloc[0]), sep='')
dic = {'(0, 500]': '近',
       '(500, 1000]': '较近',
       '(1000, 2000]': '远'}
data['等宽划分距离(映射后)'] = data['等宽划分距离'].map(dic)