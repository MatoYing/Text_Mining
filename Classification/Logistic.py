from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report  # 查看精确率、召回率、F1-score（精确率和召回率的调和平均数，是分类问题的一个衡量指标）
from sklearn.metrics import roc_auc_score, roc_curve  # ROC和AUC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 逻辑回归与二分类
# 1.读取数据（癌症案例）
column_name = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
                'Normal Nucleoli', 'Mitoses', 'Class']
data = pd.read_csv("breast-cancer-wisconsin.data", names=column_name)  # tab
# 2.缺失值处理（把？换成NaN，dropna会删掉有NaN的值）
data = data.replace(to_replace="?", value=np.nan)
data = data.dropna()
# print(data.isnull().any())    # 查看有无空值
# 3.划分数据集
x = data.iloc[:, 1:-1]
y = data["Class"]
x_train, x_test, y_train, y_test = train_test_split(x, y)
# 4.特征工程--标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# 5.预估器流程：逻辑回归
estimator = LogisticRegression()
estimator.fit(x_train, y_train)
# 逻辑回归的系数和偏置
print(estimator.coef_, estimator.intercept_)
# 6.模型评估
# 1）直接比
y_predict = estimator.predict(x_test)
print(y_test == y_predict)
# 2）计算准确率
score = estimator.score(x_test, y_test)
print(score)
##################################
# 精确率：查的全不全
# 召回率：查的对不对
report = classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"])
print(report)
##################################
# 上面的东西，举个例子，100个样本，只有一个坏的，你全蒙好的，都能达到99%，下面ROC、AUC就是为避免这个
# ROC和AUC（面积）
y_true = np.where(y_test > 3, 1, 0)  # 这里的y_test是2和4，算ROC和AUC最好是1、0，这个where就是可以讲>3的转为1，小于的转为0
# roc_auc_score第一个参数需要变为0和1，第二个不用
print(roc_auc_score(y_true, y_predict))
# Roc曲线点
fpr, tpr, thresholds = roc_curve(y_true, y_predict)  # 注意这里和roc_auc_score一样
print(fpr)
print(tpr)

# 图形绘制
plt.subplots(figsize=(8, 5))  # 新建画布
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve(area = %0.4f)' % roc_auc_score(y_true, y_predict))  # lw：线的宽度;ROC曲线
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')  # 绘制对角线
plt.xlim([0.0, 1.0]) # 指定下x轴的刻度范围
plt.ylim([0.0, 1.05])  # 指定下y轴的刻度范围
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('Train ROC Curve')
plt.legend(loc='lower right')  # 显示图例及其位置
plt.show()

