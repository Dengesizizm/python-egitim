from functions import hypotenuse as hyp

my_triangle_lengths = [(3, 4), (5, 12), (7, 24)]

# print(hypotenuse(my_triangle_lengths[0][0], my_triangle_lengths[0][1]))

for element in my_triangle_lengths:
    print(hyp(element[0], element[1]))