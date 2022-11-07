# A program that multiplies the values in a list by 2 and returns the output as a list

def list_two(lsts1):
    for i in range(len(lsts1)):
        lsts1[i] = lsts1[i] * 2  # this ensures the values are multiplied by 2 and remain in the list
        #print(lsts1[i])


def list_one():
    lst = [2, 3, 45]
    print(lst) # prints original list
    list_two(lst) # calls the function list_two and uses the lst as the argument while executing the function
    print(lst) # prints modified list

list_one()
    
