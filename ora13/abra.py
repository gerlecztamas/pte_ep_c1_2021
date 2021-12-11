from matplotlib.pyplot import *

number_of_points = 100
x, y1, y2, y3 = [], [], [], []
for i in range(number_of_points):
    x.append(i)
    y1.append(i)
    y2.append(i**2)
    y3.append(i**3)
plot(x, y1, "ro", label="y = x")
plot(x, y2, "bs", label="y = x^2")
plot(x, y3, "g", label="y = x^3")
axis([0, 10, 0, 30])
grid(True)
title("My diagram")
xlabel("x")
ylabel("y")
legend()
show()