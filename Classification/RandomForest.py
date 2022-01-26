from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
'''
集成学习
1）同质学习器集成（同一个模型，不同参数）
2）异质学习器集成

模型的线性集成
1）平均策略：随机森林
2）加权策略：GBDT
模型的非线性集成
Stacking（多个模型）
'''
boston = load_boston()
x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target)
estimator = RandomForestRegressor()
estimator.fit(x_train, y_train)
y_predict = estimator.predict(x_test)
error = mean_squared_error(y_test, y_predict)
print(error)


# 调节参数，决策树的棵树
error_list = []
for i in range(10, 200, 10):
    estimator = RandomForestRegressor(n_estimators=i, random_state=90)  # 给个随机种子，因为随机森林每次出来的数据都是随机的，避免干扰
    estimator.fit(x_train, y_train)
    y_predict = estimator.predict(x_test)
    error_list.append(mean_squared_error(y_test, y_predict))
print(error_list)


x = list(range(10, 200, 10))
plt.plot(x, error_list)
plt.ylabel('MSE')
plt.xlabel('n_estimators')
plt.show()