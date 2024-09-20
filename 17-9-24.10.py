import math
from functools import reduce

n = int(input("Enter N value: "))
numbers = [int(input(f"Number {i+1}: ")) for i in range(n)]

gcd = reduce(math.gcd, numbers)
lcm = reduce(lambda x, y: x * y // math.gcd(x, y), numbers)

print(f"LCM = {lcm}")
print(f"GCD = {gcd}")
