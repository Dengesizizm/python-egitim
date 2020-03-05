from prettytable import PrettyTable


def print_table(list):
    p = PrettyTable()
    for row in list:
        p.add_row(row)
    print(p.get_string(header=False, border=False))

def is_occupied(list, seat):
    if seat == 2:
        print("\nIts occupied!\n")
    elif seat == 0:
        print("\nThere is no seat here!\n")
    else:
        print("\nThis seat is empty!\n")
        response = input("Do you want to reserve this place? y/n  ")
        if response == "y":
            reserve(list, seat)


def reserve(list, seat):
    if list[seat[0]][seat[1]] != 1:
        print("\nYou cannot reserve this place!\n")
    else:
        print("\nYou reserved this place!\n")
        list[seat[0]][seat[1]] = 2
        print_table(list)

def cancel_res(list, seat):
    if list[seat[0]][seat[1]] == 2:
        print("\nYou canceled your reservation!\n")
        list[seat[0]][seat[1]] = 1
        print_table(list)
    elif list[seat[0]][seat[1]] == 1:
        print("\nThis place is already empty!\n")
    else:
        print("\nThere is no seat here!\n")