def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True
try:
    nums = list(map(int, input("Enter numbers: ").split()))
    primes = sum(is_prime(n) for n in nums if n > 1)
    composites = sum(not is_prime(n) and n > 1 for n in nums)
    print(f"Composite numbers: {composites}\nPrime numbers: {primes}")
except ValueError:
    print("Invalid input. Enter only numbers.")
