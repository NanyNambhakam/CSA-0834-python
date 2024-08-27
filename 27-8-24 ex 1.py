def remove_duplicates(arr):
    count = {}
    
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    result = [num for num, cnt in count.items() if cnt == 1]
    
    return result

array = [15, 14, 25, 14, 32, 14, 31]

output = remove_duplicates(array)
print("Array after removing duplicates:", output)
