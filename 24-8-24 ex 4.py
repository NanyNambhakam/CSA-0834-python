def print_numbers_with_skips(M, N, K):
    current = M
    result = []
    
    while current <= N:
        result.append(current)
        current += K + 1  # Skip K numbers
    
    return result

# Sample Input
M = 50
N = 100
K = 7

# Generate and print the output
output = print_numbers_with_skips(M, N, K)
print(", ".join(map(str, output)))
