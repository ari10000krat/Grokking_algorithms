# Сортировка массива по возрастанию


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # находит наименший элемент в массиве
        newArr.append(arr.pop(smallest))  # добавляет его в новый массив
    return newArr


print(selectionSort([4, 3, 2, 7, 2, 9, 1]))
