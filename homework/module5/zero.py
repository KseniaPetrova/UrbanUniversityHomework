def selection_sort(ls):
    for i in range(len(ls) - 1):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[min_index] > ls[j]:
                ls[min_index], ls[j] = ls[j], ls[min_index]
    return ls


data_ = [4, 5, 3, 1, 2]
print(selection_sort(data_))