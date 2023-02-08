a = list(map(int, input('Введите последовательность чисел через пробел: ').split())) #Выполнен 1ый пункт задания

def sort_bubble(array): #Определение функции сортировки
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

sort_bubble(a) #Выполнен 2ой пункт задания
print('Отсортированный список выглядит так: ', a)

#Выполнение 3го пункта задания:
def binary_search(array, element, left, right): #Определение функции алгоритма двоичного поиска
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

element = int(input('Введите число: '))
#Проверка условия ввода:
while element:
    if element <= min(a):
        print('Введено неверное число')
        element = int(input('Введите число: '))
    else:
        break

a.append(element)
sort_bubble(a)

print('Индекс числа по условию задания №3: ', binary_search(a, element, 0, len(a)-1))
