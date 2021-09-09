import pandas
from numpy import identity

# создаем матрицу 5 на 5 с нулями и единицами
inval_data = identity(5, dtype=float)
print(inval_data)

# передаем во фрейм пандас матрицу для получение объекта
data = pandas.DataFrame(inval_data)
print(data)

# создаем срезы с фрейма по 2 и 5 столбцу
col_2 = pandas.Series(data.iloc[1])
col_5 = pandas.Series(data.iloc[4])

# выводим срезы
print(col_2)
print(col_5)

# выводим тип срезов
print(type(col_2))
print(type(col_5))
