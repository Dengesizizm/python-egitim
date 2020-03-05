from theater_functions import print_table, is_occupied, reserve, cancel_res


theather = [[1, 1, 2, 2, 2, 2],
            [0, 1, 1, 2, 1, 2],
            [0, 2, 2, 1, 0, 0],
            [2, 2, 2, 2, 2, 1],
            [1, 1, 1, 2, 2, 1],
            [2, 2, 2, 1, 1, 1]]




print_table(theather)

is_occupied(theather, [0, 1])

# reserve(theather, [0, 1])
#
# cancel_res(theather, [0, 5])

# print_table(theather)



