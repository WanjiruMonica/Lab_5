# A program that takes in a list and produces the same list only with values greater than five

def original_list():
    list_1 = []
    number_of_values = int(input("Enter the number of values to be put into the list: ")) #specifies number of times to ask for user input
    print("Enter the values:")
    
    for i in range(0, number_of_values): # will ask for user input the number of times specified above
        figures = int(input())
        list_1.append(figures) #append adds items from the user input to a list already defined in line 2
    print(list_1)
    greater_than_five(list_1)


def greater_than_five(lists):
    for num in range(6):

        for i in lists:
            if i == num:
                lists.remove(i)
            else:
                new_list = lists

    print(new_list)
    
        

original_list()
