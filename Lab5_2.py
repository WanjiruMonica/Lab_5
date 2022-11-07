# A program that gives the products of elements in a list

def list_product():
    lst = [5, 2.5, 100, -10]
    print(lst)
    lst_product = 1 # initialization

    for i in lst:
        lst_product = i * lst_product # multiplies each element by the next for all items in the list
    print("The product of the above figures is",lst_product)
        
list_product()
