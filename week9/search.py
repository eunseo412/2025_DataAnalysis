def linearSearch(data_list, target):
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i
    return -1

def binarySearch(data_list, target):
    low = 0
    high = len(data_list) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if data_list[mid] == target:
            return mid
        elif data_list[mid] < target:
            low = mid + 1
        else : high = mid - 1
    
    return -1

test_list = [1, 2, 5, 8, 10, 12]
target1 = 8
index1 = binarySearch(test_list, target1)
target2 = 10
index2 = binarySearch(test_list, target2)


print(f"target1: {target1}, index1: {index1}")
print(f"target2: {target2}, index2: {index2}")