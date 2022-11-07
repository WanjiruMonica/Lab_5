# A program to show that modifying the elements of a list is not the same as modifying the list varisble itself.
# This first shows modifying the list variable itself

def list_change(lst1):
    lst1 = [1,2,3]

def main():
    lst = [6,7,8]
    print(lst)
    list_change(lst)
    print(lst)


main()
print()

# This second part shows modifying elements of the list

def list_change2(lst1):
    for i in range(len(lst1)):
        lst1[i] = lst1[i] * lst1[i]

def main2():
    lst = [6,7,8]
    print(lst)
    list_change2(lst)
    print(lst)


main2()
