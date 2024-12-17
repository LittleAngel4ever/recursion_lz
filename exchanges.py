# функция для поиска всех возможных перестановок эл-тов списка
def permutation(s): # если длина списка равна 1 то возвращаем список
    if len(s) == 1:
        return [s]

    perm_list = [] # список перестановок
    for a in s:
        remaining_elements = [x for x in s if x != a]
        z = permutation(remaining_elements) # 

        for t in z:
            perm_list.append([a] + t)

    return perm_list

# функция, в которой происходит ввод размера списка, заполнение списка элементами и вывод всех возможных перестановок эл-тов списка
def main():
    n = int(input('Введите размер списка:'))
    array = [i+1 for i in range(n)]
    print('Все возможные перестановки элементов списка: ')
    for line in permutation(array):
        print(line)


main() # вызов функции main