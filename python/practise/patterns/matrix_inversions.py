# Counting the number of inversions in a matrix
#Num of inversions = num of unordered pairs :
# {(i,j),(p,q)} such that M[i][j]> M[p][q] & i<=p & j<=q.



def row_inv(a):
    count=0
    for row in range(len(a)):
        for i in range(len(a[row])):
            for j in range(i+1,len(a[row])):
                if a[row][i] > a[row][j]:
                    count+=1
    return count


def col_inv(a):
    count=0
    for col in range(len(a)):
        for i in range(len(a[col])):
            for j in range(i+1,len(a[col])):
                if a[i][col] > a[j][col]:
                    count+=1
    return count

def diag_inv(a):
    for row in range(len(a)):
        i,j=row,0
        diag_list = []
        row_count=0
        while(i<(len(a)) and j<len(a)):
            diag_list.append(a[i][j])
            i+=1
            j+=1
        row_count += inv_counter(diag_list)
        del diag_list[:]

    for col in range(1,len(a)):
        i,j = 0,col
        diag_list = []
        col_count=0
        while(i<len(a) and j<(len(a)-1)):
            diag_list.append(a[i][j])
            i+=1
            j+=1
        #col_count += inv_counter(diag_list)
        del diag_list[:]
    return row_count +col_count

def inv_counter(diag_list):
    count=0
    for val in diag_list:
        print(val)
    for i in range(len(diag_list)):
        for j in range(i+1,len(diag_list)):
            if a[i] > a[j]:
                count+=1
    return count

    
    
                    
a = [[3,1,8],
     [7,5,6],
     [9,4,2]]

#row_count = row_inv(a)
#col_count= col_inv(a)
#diag_count = diag_inv(a)

#result = row_count + col_count+ diag_count
print(diag_inv(a))
#print(inv_counter(a))
#print(row_inv(a))
#print(col_inv(a))
