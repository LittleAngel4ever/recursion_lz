# функция для поиска НОДа
def pascal_triangle(rows):
    if rows == 1:  #если аргумент 1, то возвращаем 1
        return [[1]]
    triangle = pascal_triangle(rows - 1)
    last_row = triangle[-1]  #последняя строка из предыдущего треугольника
    new_row = [1] + [last_row[i - 1] + last_row[i] for i in range(1, len(last_row))] + [1] #перебираем пары и добавляем по крайм 1
    return triangle + [new_row]  #возвращаем новый треугольник

# функция, в которой происходит ввод чисел для поиска НОДа и вывод НОДа в консоль
def main():
    rows = int(input('Введите число уровней: ')) 
    print('pascal_triangle (',rows,') = ')    
    print(pascal_triangle(rows))


main() # вызов функции main