from sklearn.datasets import load_iris, load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor  # 分类和回归两种
from sklearn.metrics import roc_auc_score
from sklearn.metrics import mean_squared_error
# 用决策树对鸢尾花进行分类
# 信息增益（平均互信息量）= 原有的不确定性 - 尚存在的不确定性，前者固定，后者越小即信息增益越大，说明这个特征更能影响决策效率
# 1）获取数据集
iris = load_iris()
# 2）划分数据集
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)
# 3）特征工程：标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# 4）决策树
estimator = DecisionTreeClassifier(criterion="entropy")  # 默认是gini，这个是增益熵
estimator.fit(x_train, y_train)
# 5）模型评估
score = estimator.score(x_test, y_test)
print(score)
######################################
# 1)获取数据
boston = load_boston()
# 2)划分数据集
x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=22)
# 3)标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# 4)预估器
estimator = DecisionTreeRegressor(max_depth=9, max_leaf_nodes=9)
# max_depyh：决策树的最大深度
# min_samples_split：当结点中的样本数量大于这个数，才进行分裂
# min_samples_leaf：叶子结点数最少的样本数，当叶子结点比这个样本数少时，就返回上一个结点作为叶子结点
# max_leaf_nodes：叶子结点的最大数量
# min_weight_fraction_leaf：和min_samples_leaf类似，这时候样本不是等权的
# 总的来说：过拟合时把max调低，min调高；反之
estimator.fit(x_train, y_train)
# 5)模型评估
y_predict = estimator.predict(x_test)
error = mean_squared_error(y_test, y_predict)  # 均方误差（代价函数一种）
print("均方误差为：\n", error)