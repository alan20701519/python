# -*- coding: utf-8 -*-
import matplotlib.pyplot as pl
from matplotlib.ticker import MultipleLocator, FuncFormatter
import numpy as np
x = np.arange(0, 4*np.pi, 0.01)
y = np.sin(x)
pl.figure(figsize=(8,4))
pl.plot(x, y)
ax = pl.gca()

def pi_formatter(x, pos):
    """
    比較囉嗦地將數值轉換為以pi/4為單位的刻度文本
    """
    m = np.round(x / (np.pi/4))
    n = 4
    if m%2==0: m, n = m/2, n/2
    if m%2==0: m, n = m/2, n/2
    if m == 0:
        return "0"
    if m == 1 and n == 1:
        return "$\pi$"
    if n == 1:
        return r"$%d \pi$" % m
    if m == 1:
        return r"$\frac{\pi}{%d}$" % n
    return r"$\frac{%d \pi}{%d}$" % (m,n)

# 設置兩個坐標軸的範圍
pl.ylim(-1.5,1.5)
pl.xlim(0, np.max(x))

# 設置圖的底邊距
pl.subplots_adjust(bottom = 0.15)

pl.grid() #開啟網格

# 主刻度為pi/4
ax.xaxis.set_major_locator( MultipleLocator(np.pi/4) )

# 主刻度文本用pi_formatter函數計算
ax.xaxis.set_major_formatter( FuncFormatter( pi_formatter ) )

# 副刻度為pi/20
ax.xaxis.set_minor_locator( MultipleLocator(np.pi/20) )

# 設置刻度文本的大小
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(16)
pl.show()
