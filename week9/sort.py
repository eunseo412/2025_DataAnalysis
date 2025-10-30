def selectionSort(data_list, descending=False):
    n = len(data_list)

    for i in range(n - 1):
        target_index = i
        for j in range(i + 1, n):
            # 내림차순
            if descending:
                if data_list[j] > data_list[target_index]:
                    target_index = j

            # 오름차순
            else:
                if data_list[j] < data_list[target_index]:
                    target_index = j
            tmp = data_list[i]
            data_list[i] = data_list[target_index]
            data_list[target_index] = tmp
    return data_list


test_list = [5, 2, 8, 1, 9, 4]
# result1 = selectionSort(test_list)
# print(result1)
# result2 = selectionSort(test_list, descending=True)
# print(result2)


def bubbleSort(data_list, decending=False):
    n = len(data_list)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            # 내림차순
            if decending:
                if data_list[j] < data_list[j + 1]:
                    data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
            # 오름차순
            else:
                if data_list[j] > data_list[j + 1]:
                    data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
    return data_list     

result = bubbleSort(test_list, decending=True)
print(result)