import numpy as np
import matplotlib.pyplot as plt

# y = x**2
x = np.linspace(-20, 20, 100)
print(x)


def func(x):
    y = []
    for elem in x:
        # result = elem**2
        result = 1 - ((elem**2)/2)
        y.append(result)

    return y


y = func(x)

plt.plot(x, y)
plt.show()

# x = np.arange(0, 3, 0.1)
# y = x**2
# y_2 = 5*(x**2)+6*(x)+3
# y_3 = 1-((x**2)/2)
