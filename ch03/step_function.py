# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def step_function(x): # 벡터에 적용하기 위해 사용
    return np.array(x > 0, dtype=int)

X = np.arange(-5.0, 5.0, 0.1)
Y = step_function(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1)  # y축의 범위 지정
plt.show()


