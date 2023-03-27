import numpy as np

a = np.array([[4, 2, -5], [5, -6, 2], [3, 4, 3]])
b = np.array([7, -3, 5])
x = np.array([0, 0, 0])

for i in range(1000):
    x_new = np.array([0, 0, 0])
    x_new[0] = (1/a[0,0]) * (b[0] - a[0,1]*x[1] - a[0,2]*x[2])
    x_new[1] = (1/a[1,1]) * (b[1] - a[1,0]*x_new[0] - a[1,2]*x[2])
    x_new[2] = (1/a[2,2]) * (b[2] - a[2,0]*x_new[0] - a[2,1]*x_new[1])

    if np.all(np.less(np.abs(x_new - x), 0.001)):
        break
    x = x_new

print("Hasil X: ", x)