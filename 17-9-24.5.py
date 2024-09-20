def Mth_max_Nth_min(arr, M, N):
    arr = sorted(set(arr)) 
    if 0 < M <= len(arr) and 0 < N <= len(arr):  
        Mth_max = arr[-M]  
        Nth_min = arr[N-1]  
        Sum = Mth_max + Nth_min
        Difference = Mth_max - Nth_min
        return f"{M}th Maximum Number = {Mth_max}, {N}th Minimum Number = {Nth_min}, Sum = {Sum}, Difference = {Difference}"
    return "Invalid M or N"
arr = [14, 16, 87, 36, 25, 89, 34]
M, N = 1, 3
print(Mth_max_Nth_min(arr, M, N))
