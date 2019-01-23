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
    return array


def insertion_sort(array):
    for index in range(1, len(array)):
        currentvalue = array[index]
        position = index
        while position > 0 and array[position - 1] > currentvalue:
            array[position] = array[position - 1]
            position = position - 1
        array[position] = currentvalue
        print("new array is:" + str(array))
    return array

def print_string(str):
    if len(str) == 0:
        return
    head = str[0]
    print(head)
    print_string(str[1:])


def merge_sort(array):
    if len(array) < 2:
        print("a is " + str(array))
        return array
    else:
        print("b is " + str(array))
        a = merge_sort(array[:(len(array)//2)])
        b = merge_sort(array[len(array)//2:])
        array = merge(a, b)
        return array


def merge(array1, array2):
    # print("array1 is " + str(array1))
    # print("array2 is " + str(array2))
    new_array = []
    i = int(0)
    j = int(0)
    while i < len(array1) or j < len(array2):
        if i == len(array1):
            temp_value = sys.maxsize
        else:
            temp_value = array1[i]
        while j < len(array2) and temp_value > array2[j]:
            new_array.append(array2[j])
            j = j + 1
        if i < len(array1):
            new_array.append(array1[i])
            i = i + 1
    # print("new_array is :" + str(new_array))
    return new_array


def quick_sort(ray):
    if len(ray) < 2:
        return ray
    else:
        pivot, array = partition(ray)
        a = quick_sort(array[:pivot+1])
        # print("a is :" + str(a))
        b = quick_sort(array[pivot+1:])
        # print("b is :" + str(b))
        return a + b


def partition(ray):
    headray = []
    tailray = []
    index = 0
    pivot = ray[0]
    for i in range(1, len(ray)):
        if ray[i] < pivot:
            # print("index is :"+ str(i))
            headray.append(ray[i])
            index = i-1
        else:
            tailray.append(ray[i])
    headray.append(pivot)
    newray = headray + (list(reversed(tailray)))
    # print(newray)
    # print(index)
    return index, newray


def quick_sort1(ray):
    if len(ray) < 2:
        return ray
    else:
        pivot, array = partition1(ray)
        a = quick_sort1(array[:pivot])
        b = quick_sort1(array[pivot+1:])
        return a + b


def partition1(ray):
    pivot = 0
    leftindex = 0
    rightindex = len(ray)
    flag = 1
    while leftindex < rightindex:
        print("leftindex :" + str(leftindex))
        print("rightindex :" + str(rightindex))
        print("pivot :" + str(pivot))
        if flag == 1:
            for i in range(rightindex-1, -1, -1):
                print("i is :" + str(i))
                if ray[i] < ray[pivot]:
                    print("ray[i] is :" + str(ray[i]))
                    print("ray[pivot] is :" + str(ray[pivot]))
                    ray[i], ray[pivot] = ray[pivot], ray[i]
                    print("ray is :" + str(ray))
                    rightindex = i
                    pivot = i
                    flag = 0
                    break
        if flag == 0:
            for j in range(leftindex, pivot):
                if ray[j] > ray[pivot]:
                    print("ray[j] is :" + str(ray[j]))
                    print("ray[pivot] is :" + str(ray[pivot]))
                    ray[j], ray[pivot] = ray[pivot], ray[j]
                    leftindex = j
                    pivot = j
                    flag = 1
                    break
    return pivot, ray


def get_color(array):
    red = [255, 0, 0]
    green = [0, 255, 0]
    blue = [0, 0, 255]

    reddis = math.sqrt((array[0]-red[0])**2 + (array[1]-red[1])**2 + (array[2]-red[2])**2)
    greendis = math.sqrt((array[0]-green[0])**2 + (array[1]-green[1])**2 + (array[2]-green[2])**2)
    bluedis = math.sqrt((array[0]-blue[0])**2 + (array[1]-blue[1])**2 + (array[2]-blue[2])**2)

    print("reddis is " + str(reddis) + " greendis is " + str(greendis) + " bluedis is " + str(bluedis))
    mindis = min(reddis, greendis, bluedis)
    print(mindis)
    if mindis == reddis:
        print("color is red")
    elif mindis == greendis:
        print("color is green")
    elif mindis == bluedis:
        print("color is blue")


def aaaa(ray):
    print(len(ray))
    for i in range(len(ray)-1, -1, -1):
        print(i)


get_color([100, 150, 180])

# print(partition1([8,7,4,5,6]))
# print(quick_sort([98,45,33,7,0,8, 4, 5, 3, 12, 9]))
# print(quick_sort([98,5]))
#
# print(quick_sort([]))
# print(quick_sort([1]))
# print (quick_sort([2, 1]))
# print (quick_sort([1, 2, 3]))
# print (quick_sort([4, 1, 2, 3]))
# print (quick_sort([-1, -2, 0, 4, 1, 2, 3]))
# print (quick_sort([-2, -1, 0]))
# print (quick_sort([16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]))









# partition ([4,3,1,5,2])
# print (quick_sort([2,3,6,4,1]))
# insertion_sort([98,45,33,7,0,8, 4, 5, 3, 12, 9])
# selection_sort([4, 3, 2, 1])
# print(insertion_sort([8,14,33,66,78,97],6))
# merge_sort([3, 6, 7, 8, 2, 4])

# print(merge([4,8,9],[5,7,10]))


# print(merge_sort([3, 6, 7, 8, 2, 4, 5]))
# print(merge_sort([3, 2]))
# print(merge_sort([3]))
# print(merge_sort([]))

# merge_sort([3, 6, 7, 8, 2, 4, 5])
# merge([3, 6],[2,4,5])

# print(merge_sort([]))
# print(merge_sort([1]))
# print (merge_sort([2, 1]))
# print (merge_sort([1, 2, 3]))
# print (merge_sort([4, 1, 2, 3]))
# print (merge_sort([-1, -2, 0, 4, 1, 2, 3]))
# print (merge_sort([-2, -1, 0]))
# print (merge_sort([16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]))