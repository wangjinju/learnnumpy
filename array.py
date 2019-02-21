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
print(np.nonzero(A))  # 函数将所有非零元素的行与列坐标分割开，重构成两个分别关于行和列的矩阵。
# (array([0,0,0,0,1,1,1,1,2,2,2,2]),array([0,1,2,3,0,1,2,3,0,1,2,3]))
np.sort(A)  # 每一行排序
np.transpose(A)
A.T  # 两种转置方法
# 特别的，在Numpy中具有clip()函数，例子如下：
print(A)
# array([[14,13,12,11]
#        [10, 9, 8, 7]
#        [ 6, 5, 4, 3]])
print(np.clip(A, 5, 9))  # 将<=5和>=9的元素重新赋值为5和9
# array([[ 9, 9, 9, 9]
#        [ 9, 9, 8, 7]
#        [ 6, 5, 5, 5]])

# 迭代输出问题
A = np.arange(3, 15).reshape((3, 4))
print(A.flatten())
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
for item in A.flat:
    print(item)
# 3
# 4
# ……
# 14
# 这一脚本中的flatten是一个展开性质的函数，将多维的矩阵进行展开成1行的数列。
# 而flat是一个迭代器，本身是一个object属性。


# array合并
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
np.hstack(A, B)  # 上下合并
np.vstack(A, B)  # 水平合并
# np.newaxis() 将序列弄成矩阵属性 可进行转置操作
print(A[np.newaxis, :])
# [[1 1 1]]
print(A[np.newaxis, :].shape)
# (1,3)
# np.concatenate()
C = np.concatenate((A, B, B, A), axis=0)  # 合并操作需要针对多个矩阵或序列时


# array分割
A = np.arange(12).reshape((3, 4))
print(A)
"""
array([[ 0,  1,  2,  3],
    [ 4,  5,  6,  7],
    [ 8,  9, 10, 11]])
"""
print(np.split(A, 2, axis=1))  # 纵向分割
"""
[array([[0, 1],
        [4, 5],
        [8, 9]]), array([[ 2,  3],
        [ 6,  7],
        [10, 11]])]
"""
print(np.split(A, 3, axis=0))  # 横向分割
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]

# 不等量的分割np.array_split()
print(np.array_split(A, 3, axis=1))
"""
[array([[0, 1],
        [4, 5],
        [8, 9]]), array([[ 2],
        [ 6],
        [10]]), array([[ 3],
        [ 7],
        [11]])]
"""
