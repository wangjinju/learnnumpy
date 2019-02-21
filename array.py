import numpy as np

# 属性
array = np.array([[1, 2, 3], [2, 3, 4]])
print(array)
array.ndim  # 维度
array.shape  # 行列数
array.size  # 元素个数

# 关键字
# array dtype zeros ones empty arrange linespace reshape
a = np.arange(12).reshape((3, 4))    # 3行4列，0到11
a = np.linspace(1, 10, 20)    # 开始端1，结束端10，且分割成20个数据，生成线段
a = np.linspace(1, 10, 20).reshape((5, 4))  # 更改shape

# numpy基础运算1
a = np.array([10, 20, 30, 40])   # array([10, 20, 30, 40])
b = np.arange(4)              # array([0, 1, 2, 3])
# + - * /
c = b**3  # 各个元素立方
# 调用函数运算 利用np的关键字：sin()...
c = 10*np.sin(a)
# 矩阵乘法运算dot
c_dot = s.dot(b)
# 随机生成矩阵
a = np.random.random((2, 4))
np.sum(a)
np.min(a, axis=1)  # 行查找
np.max(a, axis=0)  # 列查找
