def binary_search(a,val,l,u):
    mid = (l+u)//2
    
    # Base condition.
    if l-u==0:
        return False

    if val == a[mid]:
        return True

    elif val< a[mid]:
        return binary_search(a,val,l,mid)

    elif val> a[mid]:
        return binary_search(a,val,mid+1,u)
    
a = [x for x in range(11)]

print(binary_search(a,7,0,10))
