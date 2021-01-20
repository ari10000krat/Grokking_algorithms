from random import randint
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        rand_index = randint(0,len(array))
        pivot = array[rand_index]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    print(quicksort([5, 3, 65, 2, 8, 2, 45, 3, 6, 2]))
