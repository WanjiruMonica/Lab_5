# A program that removes from a list values that are less than five

def first_list():
    lst = [12,45,67,89,1,3] # original list
    print(lst)
    less_than_five(lst)

def less_than_five(list1):
    for numbers in range(5):  # defines the values to be removed, that is 0,1,2,3,4 if they are in the list.
        
        for i in list1:
            if i == numbers:  
                list1.remove(i)  #removes the highlighted numbers
            else:
                remainder = list1 # new list
            
    print(remainder)
            
                
first_list()
        
