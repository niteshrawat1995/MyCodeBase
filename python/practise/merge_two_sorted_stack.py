# Merge to sorted stack in to 1 sorted stack.
# Conquer part of Merge Sort.
# Using list as stack with only allowed function append(push),pop(pop).


s1 = [5,4,3,2,1]
s2 = [10,9,8,7,6]

def conquer(s1,s2):
    s3 = []
    i = len(s1)-1
    j = len(s2)-1
    
    while len(s1) or len(s2):
        # if s1 gets exhausted.
        if len(s1)==0:
            x = s2.pop()
            s3.append(x)
        # if s2 gets exhausted.
        elif len(s2)==0:
            x = s1.pop()
            s3.append(x)
            
        # logic: comparing the top element
        else:
            if s1[i] < s2[j]:
                x= s1.pop()
                s3.append(x)
                i-=1
            else:
                x=s2.pop()
                s3.append()
                j-=1
    return s3

print(conquer(s1,s2))
