import numpy as np
import time
a = np.zeros((200, 200), order='C')
b = np.zeros((200, 200), order='F')
N = 9999


def f1(a):
    for _ in range(N):
        np.concatenate((a, a), axis=0)


def f2(b):
    for _ in range(N):
        np.concatenate((b, b), axis=0)


t0 = time.time()
f1(a)
t1 = time.time()
f2(b)
t2 = time.time()

print((t1-t0)/N)     # 0.000040
print((t2-t1)/N)     # 0.000070
print(a, b)
