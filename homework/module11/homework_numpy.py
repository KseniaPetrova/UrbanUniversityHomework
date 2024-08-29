import numpy as np
"""
Библиотека NumPy позволяет выполнять разные математические операции с массивами данных. Например массивы можно 
складывать, переумножать, находить сумму по определенной оси, находить среднее значение и стандартное отклонение.
"""
arr1 = np.array([[1, 2, 3, 4, 5, 6]])  # Один из способов инициализации массива
arr2 = np.array([[8, 0, 2, 7, 3, 1]])

# сложение массивов
arr3 = arr1 + arr2
print('сложение массивов', arr3)

# умножение массивов
arr3 = arr1 * arr2
print('умножение массивов', arr3)

# сумма чисел в массиве
print('сумма чисел в массиве', arr1.sum())

# среднее значение
print('среднее значение', np.mean(arr1))

# стандартное отклонение
print('стандартное отклонение', np.std(arr1))

