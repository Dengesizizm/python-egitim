my_list = [123, 346, 786, 12, 6456, 234]

# sliced_list = my_list[1:-1]
#
# print(sliced_list)
my_other_list = ["abc", "gj234", "89374"]

# my_list.append(my_other_list)

# my_list[0] = 321

my_very_other_list = list(my_list)

my_very_other_list[0] = "different"


print(my_very_other_list)

print(my_list)