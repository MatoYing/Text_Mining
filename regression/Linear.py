# pip安装
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# 梯度下降法三个注意点
# 1.步长（学习率）的大小：可以前期较大，后期较小
# 2.可能陷入局部最优：取多个初始值
# 3.量纲影响：特征处理

# 正规方程的优化方法
# 1)获取数据
boston = load_boston()
# 2)划分数据集
x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2, random_state=22)
# 3)标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# 4)预估器
estimator = LinearRegression()
estimator.fit(x_train, y_train)
# 5)得出模型
print("权重系数为：\n", estimator.coef_)
print("偏置为：\n", estimator.intercept_)
# 6)模型评估
y_predict = estimator.predict(x_test)  # 这里要注意上面拿出来的x_test其实是二维的数组，你放一个一维的也能算，不过二维的更好
error = mean_squared_error(y_test, y_predict)  # 均方误差MSE（代价函数一种），越小越好
print("均方误差为：\n", error)

y_test_predict = estimator.predict(x_train)
test_error = mean_squared_error(y_train, y_test_predict)
print("测试集均方误差\n", test_error)

# R方法(越接近1越好)
error_R = r2_score(y_test, y_predict)
print("R方：\n", error_R)


x = list(range(len(y_test)))
plt.plot(x, y_test, label='true')  # 实际的y
plt.plot(x, y_predict, label='pred')  # 预测的y
plt.show()

# 泛化能力：模型对位遇见过数据的预测能力
# 泛化误差：偏差+方差+噪声
# 交叉验证：就是所有的数据分组，一会当测试集，一会当训练集，一般不用，用70%训练集，30%测试集