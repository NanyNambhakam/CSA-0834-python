def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime_composite(numbers):
    prime_count = 0
    composite_count = 0
    
    for number in numbers:
        if is_prime(number):
            prime_count += 1
        elif number > 1:  # Composite numbers are greater than 1
            composite_count += 1
            
    return prime_count, composite_count

def main():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    
    prime_count, composite_count = count_prime_composite(numbers)
    
    print(f"Prime numbers count: {prime_count}")
    print(f"Composite numbers count: {composite_count}")

if __name__ == "__main__":
    main()
