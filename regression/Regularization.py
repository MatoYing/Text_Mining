import pylab as pl
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
"""
如何防止过拟合？
答：增加正则化项，减少模型复杂度（减少高次项？）（奥卡姆剃刀原则：用尽量简单的模型，提升泛化能力）
1.Ridge回归
2.Lasso回归
3.Elastic回归
加入不同的正则项，都对模型的复杂度予以限制：α越大则约束越强，拟合能力越弱
"""

# 1)获取数据
boston = load_boston()
# 2)划分数据集
x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=22)
# 3)标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

alphas = [0.001, 0.005, 0.1, 0.2, 0.3, 0.4, 0.5, 1, 1.5]
mse_train = []
mse_tests =[]
for alpha in alphas:
    # 4)预估器
    estimator = Lasso(alpha=alpha)
    estimator.fit(x_train, y_train)
    # 5)模型评估
    y_train_pred = estimator.predict(x_train)
    error_train = mean_squared_error(y_train, y_train_pred)
    mse_train.append(error_train)
    y_test_pred = estimator.predict(x_test)
    error_test = mean_squared_error(y_test, y_test_pred)
    mse_tests.append(error_test)
plt.plot(alphas, mse_train, label='train')
plt.plot(alphas, mse_tests, label='test')
plt.show()
