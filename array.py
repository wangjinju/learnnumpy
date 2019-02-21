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

# numpy基础运算2
A = np.arange(2, 14).reshape((3, 4))
# array([[ 2, 3, 4, 5]
#        [ 6, 7, 8, 9]
#        [10,11,12,13]])
print(np.argmin(A))    # 0 求最小元素索引
print(np.argmax(A))    # 11 求最大元素索引
A.mean()  # 或者 np.mean(A)
A.average()
A.median()
np.mean(A)
# 在cumsum()函数中：生成的每一项矩阵元素均是从原矩阵首项累加到对应项的元素之和。
# 比如元素9，在cumsum()生成的矩阵中序号为3，即原矩阵中2，3，4三个元素的和。
print(np.cumsum(A))
# [2 5 9 14 20 27 35 44 54 65 77 90]
print(np.diff(A))  # 累差函数：每一行中后一项与前一项之差
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]
