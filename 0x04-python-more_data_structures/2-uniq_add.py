def uniq_add(my_list=[]):
    matrix_list = set()

    for x in my_list:
        matrix_list.add(x)

    return sum(matrix_list)
