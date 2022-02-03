"""
seaborn是在matplotlib的基础上进行了更高级的API封装，从而使得作图更加容易，在大多数情况
下使用seaborn能做出很具有吸引力的图，而使用matplotlib就能制作具有更多特色的图。应该把seaborn
视为matplotlib的补充
"""
# 千万别起和报名一样的文件名，否则import是会认为是在引你写的呢个文件
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle
import warnings
from pylab import *


def f1(data):
    # 记得修改一下画布，否则显示不全
    plt.figure(figsize=(15, 10))
    sns.countplot(data['Outcome'])
    # sns.countplot(data['Pregnancies'])
    plt.title('糖尿病正负样本分布')
    plt.show()


def f2(data):
    # 直方图
    plt.hist(data['Glucose'], bins=50)  # 分的更细
    plt.show()


def f3(data):
    # 新建画布
    _, axes = plt.subplots(4, 2, figsize=(15, 10))
    # 设置画布
    axes = axes.flatten()
    ax_idx = 0
    # 对每一列进行直方图绘制
    for col in data.columns[:-1]:
        # 绘制直方图
        data[col].plot(kind='hist', ax=axes[ax_idx], title=col, color=next(color_cycle), bins=50)
        ax_idx += 1
    # 大标题
    plt.suptitle('各特征分布情况')
    # 调节下分布，图与图可能重合
    plt.tight_layout()
    plt.show()


def f4(data):
    sns.distplot(df[df['Outcome'] == 0]['Age'], kde=True)  # ==0的拿出来后的data在取Age
    sns.distplot(df[df['Outcome'] == 1]['Age'], kde=True)
    plt.show()


def f5(data):
    # 箱型图
    sns.boxplot(x='Outcome', y='Age', data=data)
    plt.show()


def f6(data):
    # 散点图
    sns.jointplot(data=df, x='Age', y='BloodPressure', kind='reg')
    plt.show()


def f7(data):
    # 相关系数图(颜色越深越相关)
    corr = data.corr()  # 两个变量之间的相关性
    plt.figure(figsize=(6, 6))
    sns.heatmap(corr, vmax=1.0, square=True, annot=True, cmap='YlGnBu')
    plt.show()


if __name__ == '__main__':
    # 画图风格
    plt.style.use('fivethirtyeight')
    # 设置颜色风格
    color_cycle = cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])
    # 忽略警告
    warnings.filterwarnings('ignore')
    # 显示中文
    # plt.rcParams['font.sans-serif'] = ['SimHer']   不能用
    mpl.rcParams['font.sans-serif'] = u'SimHei'
    # 用来正常显示负号
    plt.rcParams['axes.unicode_minus'] = False

    df = pd.read_csv('diabetes.csv')
    # f1(df)
    # f2(df)
    f3(df)
    # f4(df)
    # f5(df)
    # f6(df)
    # f7(df)