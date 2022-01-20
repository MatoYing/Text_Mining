import pandas as pd
import numpy as np

# pandas中有两种常用的基本结构
# Series：一维数组
# DataFrame：二维的表格型数据结构

s = pd.Series([1, 3, 5, np.nan, 6, '8'])
print(s)
print(s.index)
print(s.values)

# 读取并查看数据
# 注意安装xlrd包
df = pd.read_excel('test.xls')
print(df)
# 数据信息
print(df.info())
# 头尾数据
print(df.head(3))  # 默认是5个
print(df.tail())
# 第一列序号，行标题
print(df.index)
print(df.columns)

print(df.iloc[0, 5])  # 从第0个到第5个
print(df.loc[0:1])  # 从索引0到5；不能像iloc一样指定行
# 删除
# df.drop([30])
# df = df.drop('考生姓名', axis=1)  # axis=1代表列，0代表行

# 查看多列
print(df[['考生姓名', '报考类别']][:5])

# 条件选择
print(df[df['考生姓名'] == '小明'])
print(df[df.考生姓名 == '小明'])
print(df[(df.考生姓名 == '小明') & (df.报考类别 == '理工')])  # 一定记得加括号

# 排序
df.sort_values(by='高考成绩', ascending=False)
print(df)

# 基本统计分析
print(df.describe())
print(df['高考成绩'].max())
print(len(df))
print(df['高考成绩'].unique())
print(df['高考成绩'].value_counts())  # 每个成绩有几个

# 数据保存
# df.to_excel('new_test.xlsx', index=None)  # 不要index

