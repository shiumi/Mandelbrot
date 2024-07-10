import numpy as np
import matplotlib.pyplot as plt

# Определение функции Мандельброта
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Параметры изображения
width = 1000
height = 1000
max_iter = 30 # качество изображения / скорость генерации

# Решетка комплексных чисел
x = np.linspace(-2, 1, width)
y = np.linspace(-1, 1, height)
X, Y = np.meshgrid(x, y)
C = X + 1j*Y

# Вычисление точек
M = np.zeros((width, height))
for i in range(width):
    for j in range(height):
        M[i, j] = mandelbrot(C[i, j], max_iter)


# Визуализация
plt.imshow(M, cmap='bone')
plt.title('Множество Мандельброта')
plt.show()
