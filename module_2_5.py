def get_matrix(n, m, value): # Задаем функцию
    matrix = []  # Создаем пустой список внутри функции
    for i in range(n):
        matrix.append([])  # Добавляем количество пустых списков в соотв-ии с 'n'
        for j in range(m):
            matrix[i].append(value)  # Добавляем 'value' в списки[i] в соотв-ии с 'm'
    print(matrix)
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
# Если закомментировать 3 последних строки, то None не будет выводиться,
