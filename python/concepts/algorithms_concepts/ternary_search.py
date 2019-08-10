# Ternary search divides the list into 3 parts instead of 2 in case of binary search.\
# Time complexity =0(n/3)
#Space Complexity =0(1)

def ternary_search_iterative(seq,key):
    low = 0
    high = len(seq)-1 #9-1 =8


    while low < high:
        # Defining 2 midpoints which will divide the list in 3 parts.
        midFirst = low + (high-low)//3
        midSecond = midFirst + (high-low)//3 # 2+2 =4

        if seq[midFirst] == key:
            return midFirst
        if seq[midSecond] == key:
            return midFirst
        
        if key < seq[midFirst]:
            high = midFirst-1
        if key > seq[midSecond]:
            low = midSecond+1
            
        else:
            low = midFirst+1
            high = midFirst-1
            
    return None
'''
l      m1      m2              h
1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9

m2
m1
l      h             
1, 2 , 3 , 4 ,5 , 6 , 7 , 8 , 9
'''


#Driver
seq = [1,2,3,4,5,6,7,8,9]
print(ternary_search_iterative(seq,5))


            
    
    
    
