import numpy as np

a = [1, 2, 3, 4]
# 平均值
print(np.mean(a))

# 列表转数组（numpy特有）
a = np.array(a)
print(a + 1)

# 一维转二维
b = np.array([[1, 2, 3], [2, 3, 4]])
print(b)

# zeros数组
b = np.zeros(5)
c = np.zeros((2, 3))
print(b)
print(c)

# ones数组
b = np.ones(5)
c = np.ones((2, 3))
print(b)
print(c)

# 序列数组
a = np.arange(2, 10, 2)
print(a)

# 随机数组（能取到下限，取不到上限）
a = np.random.uniform(2, 10, 10)
b = np.random.uniform(2, 10, size=(2, 3))
c = np.random.randint(0, 100, 10)
print(a)
print(b)
print(c)

# 数组属性
print(a.shape)  # 行与列
print(a.size)  # 元素个数

# 在数组中切片的本质是引用，a改变后b也会改变；列表则不是
a = np.array([1, 2, 3, 4])
b = a[1:3]
b = a[1:3].copy()  # 这样就不是引用

# 特殊切片
print(a[a > 10])

# 限定两位小数
print(np.round(a, 2))
# 将一维变二维
print(a.reshape(2, 2))

# 按行排序（得array）
a = np.random.randint(1, 100, size=(3, 4))
a = np.array(a)
a.sort(1)
print(a)
# 按列排序（得array）
a.sort(0)
print(a)