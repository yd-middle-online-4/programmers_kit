def value_list(list_1):
    result_value = list_1[0]
    result_list_value = list_2[0]
    for list_test in list_1:
        if list_test < result_list_value:
            result_value = list_test
    return result_list_value

list_1 = [1,55,23,23]
list_2 = [4,24,78,6,21]

print("first value in list_1 is ",value_list(list_1))
print("Second value in list_2 is ",value_list(list_2))
