"""
input1: entire family biscuit diet
input2: new family member diet

output: nearest matching diet person.

"""

#family_members_diets = list(map(int, input().strip().split(',')))
#family_members_diets = sorted(family_members_diets)
#new_member_diet = int(input())

#def closest_diet(family_members_diets, new_member_diet):
    #family_members_diets = sorted(family_members_diets)


def search(seq, i , j, x):
    mid = (i+j) // 2
    mid = int(mid)

    if i-j == 0:
        print(mid)
        possibilities = list()
        possibilities.append(abs(seq[mid-1]-x))
        possibilities.append(abs(seq[mid]-x))
        possibilities.append(abs(seq[mid+1]-x))
        index_min = min(range(len(possibilities)), key=possibilities.__getitem__)
        if index_min == 0:
            return seq[mid-1]
        elif index_min == 1:
            return seq[mid]
        else:
            return seq[mid+1]

        
    
    if x == seq[mid]:
        return seq[mid]
    elif x > seq[mid]:
        return search(seq, mid+1, j, x)
    elif x < seq[mid]:
        return search(seq, i, mid, x)

    else:
        return None


seq = [100, 50, 60, 130, 150, 250]

x = 170

result = search(seq, 0, len(seq), x)
print(result)
"""

a = [2,8,1]
index_min = min(range(len(a)), key=a.__getitem__)
print(index_min)
"""
