import numpy as np
import matplotlib.pyplot as plt;
f = open('test.txt', 'r')
content = [x.strip('\n') for x in f.readlines()]
y = []
for i in content:
    if i != '':
        y.append(int(i))
x = list(range(1,len(y)+1))
plt.figure(figsize(8,6))
plt.plot(x,y,"c.-",label="$test$",linewidth = 2,marker='o',
         markerfacecolor='blue', markersize=5)
plt.xlabel("input")
plt.ylabel("output")
plt.xlim(0,20)
plt.ylim(0,18)
#網格
#plt.grid()
plt.legend()
plt.show()
