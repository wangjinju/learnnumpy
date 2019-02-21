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
