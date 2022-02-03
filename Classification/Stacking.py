import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# 这个代码的理解需要看网上呢张图
def get_stacking(clf, x_train, y_train, x_test, n_folds=10):
    # 这个函数是stacking的核心，使用交叉验证的方法得到次级训练集
    # 计算训练集和测试集的样本数
    train_num, test_num = x_train.shape[0], x_test.shape[0]
    # 存储结果
    second_level_train_set = np.zeros(train_num)
    second_level_test_set = np.zeros(test_num)
    test_nfolds_sets = np.zeros((test_num, n_folds))
    # K折交叉验证
    kf = KFold(n_splits=n_folds)
    # 依次使用K折数据集训练数据
    for i, (train_index, test_index) in enumerate(kf.split(x_train)):
        # 切分K折数据
        x_tra, y_tra = x_train[train_index], y_train[train_index]
        x_tst, y_tst = x_train[test_index], y_train[test_index]
        # 训练数据
        clf.fit(x_tra, y_tra)
        # 对训练集和测试集进行预测
        second_level_train_set[test_index] = clf.predict(x_tst)  # 每次的test_index不会重复
        test_nfolds_sets[:, i] = clf.predict(x_test)
    # 计算返回的均值
    second_level_test_set[:] = test_nfolds_sets.mean(axis=1)  # 求每一行的平均值
    return second_level_train_set, second_level_test_set


# 需要融合的模型
rf_model = RandomForestRegressor()
dr_model = DecisionTreeRegressor()

# 存储新特征的列表
train_sets = []
test_sets = []

boston = load_boston()
x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target)

for clf in [rf_model, dr_model]:
    train_set, test_set = get_stacking(clf, x_train, y_train, x_test, n_folds=10)
    train_sets.append(train_set)
    test_sets.append(test_set)

meta_train = np.concatenate([result_set.reshape(-1, 1) for result_set in train_sets], axis=1)  # axis=1是对应行进行拼接，0是在屁股后面接上；reshape(-1, 1)转换成一列
meta_test = np.concatenate([result_set.reshape(-1, 1) for result_set in test_sets], axis=1)

# 弱学习器作为整合融合模型
dr_clf = DecisionTreeRegressor(max_depth=3)
dr_clf.fit(meta_train, y_train)
df_predict_train = dr_clf.predict(meta_train)
df_predict_test = dr_clf.predict(meta_test)
print(mean_squared_error(df_predict_train, y_train))
print(mean_squared_error(df_predict_test, y_test))