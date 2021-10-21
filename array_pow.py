import numpy as np


# Функция матричного умножения, принимающая на вход 3 матрицы
def prod_matrix(matrix1, matrix2, matrix3):
    shape1 = matrix1.shape  # определим форму 1-ой матрицы
    shape2 = matrix2.shape  # определим форму 2-ой матрицы
    shape3 = matrix3.shape  # определим форму 3-ей матрицы

    if shape1[1] != shape2[0]:  # если количество столбцов 1-ой матрицы не равно количеству строк 2-ой матрицы
        return np.array([])  # тогда умножение невозможно, возвращаем пустой массив
    if shape1[1] != shape3[0]:  # если количество столбцов 1-ой матрицы не равно количеству строк 3-ой матрицы
        return np.array([])  # тогда умножение невозможно, возвращаем пустой массив

    out_matrix = np.zeros(
        (shape1[0],
         shape2[1]))  # создадим матрицу из 0, формой (количество строк 1-ой)Х(количество столбцов 2-ой) матриц
    tot_matrix = np.zeros(
        (shape1[0],
         shape2[1]))  # создадим матрицу из 0, формой (количество строк 1-ой)Х(количество столбцов 2-ой) матриц

    for i in range(shape1[0]):  # пройдемся по индексам строк 1-ой матрицы
        for j in range(shape2[1]):  # пройдемся по индексам столбцов 2-ой матрицы
            curr_cell = 0
            for t in range(shape1[1]):  # пройдемся по индексам стобцов 1-ой матрицы
                curr_cell += matrix1[i, t] * matrix2[
                    t, j]  # посчитаем сумму произведения элементов строки 1-ой матрицы и столбцов 2-ой матрицы
            out_matrix[i, j] = curr_cell  # заменим значения в матрице состоящих из 0, на посчитанную сумму произведений
    shape4 = out_matrix.shape  # определим форму полученной матрицы
    for i in range(shape4[0]):  # пройдемся по индексам строк полученной матрицы
        for k in range(shape3[1]):  # пройдемся по индексам столбцов 3-ей матрицы
            curr_celltot = 0
            for j in range(shape4[1]):
                try:
                    curr_celltot += out_matrix[i, j] * matrix3[j, k]
                except IndexError:
                    pass
            tot_matrix[i, k] = curr_celltot
    return tot_matrix  # вернем полученную матрицу


if __name__ == '__main__':
    matrix1 = np.array([[2, 3], [1, 2], [4, 1]])  # матрица 3х2
    matrix2 = np.array([[2, 3, 4], [1, 2, 1]])  # матрица 2х3
    matrix3 = np.array([[2, 3, 3], [1, 3, 4],])  # матрица 2х3
    matrix_total = prod_matrix(matrix1, matrix2, matrix3)
    print(matrix_total)
