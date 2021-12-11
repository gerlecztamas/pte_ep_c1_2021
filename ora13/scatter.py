import matplotlib.pyplot as plt
import numpy as np

number_of_points = 100
x=np.random.randint(0, 500, number_of_points)
y=x+30*np.random.randn(number_of_points)
size = np.random.randint(0, 200, number_of_points)
color=np.random.randint(0,10,number_of_points)
plt.scatter(x,y, s=size, c=color)
plt.show()