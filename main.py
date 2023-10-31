import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math
import time
#change this value
terms = 20
def approx_sin(x, terms):
    function = 0
    for i in range(terms):
        new = ((-1)**i)*((x**((2*i)+1))/math.factorial((2*i)+1))
        function = function + new
    return function

x = np.linspace(-15, 15, 300)
y1 = np.sin(x)
y2 = np.cos(x)


fig, ax = plt.subplots()
ax.set(xlim=[-15, 15], ylim=[-10, 10], xlabel='x', ylabel='y')
line1, = ax.plot(x, y1, label='Plot 1', color='blue')
line2, = ax.plot(x, y2, label='Plot 2', color='red')


ax.legend()


for i in range(terms):
    y2 = approx_sin(x, i+1)  
    line2.set_data(x, y2)  
    plt.pause(2)  

plt.show()