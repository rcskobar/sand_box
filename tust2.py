my_array = [43, 12, 353, 543, 6, 4572, 3, 47, 7, 4]


def my_sort(my_array, revers=False):
    for i in range(len(my_array) - 1):
        for y in range(i + 1, len(my_array)):
            if revers:
                if my_array[i] < my_array[y]:
                    my_array[i], my_array[y] = my_array[y], my_array[i]
            else:
                if my_array[i] > my_array[y]:
                    my_array[i], my_array[y] = my_array[y], my_array[i]

    return my_array


print(my_sort(my_array, revers=False))
