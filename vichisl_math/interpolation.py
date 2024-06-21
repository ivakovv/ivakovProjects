import matplotlib.pyplot as plt
import numpy as np
def lagrange_iter(x, y, x_val):
    n = len(x)
    result = 0
    for i in range(n):
        y_i = y[i]
        for j in range(n):
            if j != i:
                y_i *= (x_val - x[j]) / (x[i] - x[j])
        result += y_i
    return result
x = [0, 1, 2, 5]
y = [2, 3, 12, 147]
x_args = [0, 2, 11.5, 16, 35]
for arg in x_args:
    result = lagrange_iter(x, y, arg)
    print(f'y= {result}')
fig, ax = plt.subplots()

x = np.linspace(-5, 15, 1000)

y = x**3 + x**2 - x + 2

ax.plot(x, y)
plt.ylim(-10, 10)
plt.show()