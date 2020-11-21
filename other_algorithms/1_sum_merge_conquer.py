import math

def sum(list_of_x):
    mid = math.floor(len(list_of_x)/2) 
    
    left = list_of_x[:mid]
    right = list_of_x[mid:]
    
    
    if len(list_of_x) == 1:
        return(list_of_x[0])
    else:
        return(sum(left) + sum(right))
