import numpy as np
import matplotlib.pyplot as plt

'''
折线图
条形图
直方图
饼图
'''


def line_chart():
    # 自变量+因变量+作图函数
    x = np.arange(0, 100, 0.01)  # 直线无所谓，取钱要间隔小点
    y1 = 2 * x + 1
    y2 = -2 * x + 1
    plt.figure(figsize=(12, 6))  # 改变大小
    plt.plot(x, y1, '-.', color='red', linewidth=4)
    plt.plot(x, y2, '--', color='black')
    plt.xlabel('independent variable', fontsize=16)
    plt.ylabel('dependent variable')
    plt.xticks(fontsize=12)
    plt.legend(['line one', 'line two'])
    plt.title('first plot')
    plt.grid()  # 加横线
    plt.show()
    # 还能做子图：在plt开始时加上plt.subplot(2,1,1)（2行，1列，第一个），下一个plt.subplot(2,1,2)


def bar_chart():
    company = ['Samsung', 'Huawei', 'Apple', 'Others']
    shipment = [300, 500, 1000, 50]
    plt.bar(company, shipment, width=0.5, color='royalblue')
    # 可以加个折线
    plt.plot(company, shipment, marker='o', markersize=10)
    plt.show()


def histogram():
    # 随机数直方图（就是统计每个数出现的次数）
    x1 = np.random.randint(1, 11, 100)
    # 子图：在plt开始时加上plt.subplot(2,1,1)（2行，1列，第一个），下一个plt.subplot(2,1,2)
    plt.subplot(2, 1, 1)
    plt.hist(x1)
    plt.subplot(2, 1, 2)
    # 正态分布图
    x2 = np.random.randn(10000000, 1)
    plt.hist(x2, bins=100)  # bins增多条数
    plt.show()


def pie_chart():
    company = ['Samsung', 'Huawei', 'Apple', 'Others']
    shipment = [300, 500, 1000, 50]
    x = company
    y = shipment
    plt.pie(y, labels=x, autopct='%.1f%%', textprops={'fontsize': 'x-large'}, labeldistance=1.2, shadow=True)  # labeldistance让字离pie远点
    plt.show()

if __name__ == '__main__':
    # line_chart()
    # bar_chart()
    # histogram()
    pie_chart()
