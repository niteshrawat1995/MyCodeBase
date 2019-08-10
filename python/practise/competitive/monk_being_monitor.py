print('give input')
num_of_test = int(input())
for _ in range(num_of_test):
    num_of_heights = int(input())
    heights = list(map(int, input().split(' ')))
    #print('the input heights are:')
    #print(heights)
    unique_ht = list(set(heights))  # unique heights
    #print('the unique heights are:')
    #print(unique_ht)
    height_count = {}

    # dictionary
    for height in heights:
        if height not in height_count:
            height_count[height] = 1
        else:
            height_count[height] += 1
    
    #print('the height_count are:')
    #print(height_count)
    
    result = []
    diff = 0
    for i in unique_ht:
        for j in unique_ht:
            if height_count[i] - height_count[j] == 0:
                result.append(0)
            else:
                diff = height_count[i] - height_count[j]
                if diff>0:
                    result.append(diff)
    if all(v == 0 for v in result):
        print(-1)
    else:
        print(result)
