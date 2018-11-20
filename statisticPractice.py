import math


# 平均值
def get_mean(ray: object) -> object:
    b = len(ray)
    total = 0.0
    for i in ray:
        total = total + i
    result = total / b
    print("get_mean is " + str(result))
    return result


# 中值
def get_median(array):
    new_array = sorted(array)
    size = len(new_array)
    if size % 2 == 0:
        median = (new_array[size // 2] + new_array[size // 2 - 1])/2.0
    else:
        median = new_array[(size-1) // 2]

    print("get_median is " + str(median))
    return median


# most frequently number
def get_mode(array):
    dict = {}
    for i in array:
        dict[i] = array.count(i)

    print(dict)
    print(max(dict.values()))
    result = (list(dict.keys()))[list(dict.values()).index(max(dict.values()))]
    print("get_mode is " + str(result))
    return result


# 方差
def get_variance(array):
    mean_num = get_mean(array)
    total = 0.0
    for i in array:
        total = total + (i - mean_num) * (i - mean_num)
    result = total / len(array)
    print(result)
    return result


# 标准差
def get_standard_division(array):
    result = math.sqrt(get_variance(array));
    print("get_standard_division is " + str(result))
    return result


# 协方差
def get_covariance(array1, array2):
    mean_num1 = get_mean(array1)
    mean_num2 = get_mean(array2)
    total = 0.0
    # for (i, j) in zip(array1, array2):
    #     total = total + (i - mean_num1) * (j - mean_num2)

    for i in range(len(array1)):
        total = total + (array1[i] - mean_num1) * (array2[i] - mean_num2)

    result = total / (len(array1) - 1)
    print("get_covariance is " + str(result))
    return result


# 相关性
def get_correlation(array1, array2):
    result = get_covariance(array1, array2) / (get_standard_division(array1) * get_standard_division(array2))
    print("get_correlation is " + str(result))
    return result


get_correlation([1, 2, 3, 4], [1, 2, 3, 4])