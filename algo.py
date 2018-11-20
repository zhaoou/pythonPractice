import math


# best case: value is in the first element of the array. worst case:value is not in the array or in the end of the array
def linear_search(array, value):
    result = -1
    for i in range(len(array)):
        print(array[i])
        if array[i] == value:
            result = i
    print("linear_search is " + str(result))
    return result


def binary_search(array, value):
    if len(array) == 0:
        print("failed")
        return 0

    if len(array) == 1 and array[0] != value:
        return 0

    if len(array) % 2 == 1:
        if array[int(len(array) / 2)] == value:
            print("success")
            return 1
        else:
            if array[int(len(array) / 2)] > value:
                new_array = array[0: int(len(array) / 2)]
                # print("come on1 new_array is :" + str(new_array))
            else:
                new_array = array[-int(len(array) / 2):]
            binary_search(new_array, value)
    else:
        if array[int(len(array) / 2)] > value:
            new_array = array[0: int(len(array) / 2)]
        else:
            new_array = array[-int(len(array) / 2):]
        binary_search(new_array, value)


def selection_sort(array):
    print(len(array))
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            print(j)
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]
        print("new array is:" + str(array))


def insertion_sort(array, value):
    # array.insert(10, value)
    if len(array) == 0:
        array.insert(0, value)
        print(array)
        return
    for i in reversed(range(len(array))):
        if array[i] <= value:
            array.insert(i+1, value)
            print(array)
            return



selection_sort([98,45,33,7,0,8, 4, 5, 3, 12, 9])
# selection_sort([4, 3, 2, 1])
# insertion_sort([5,86,323], 6)

