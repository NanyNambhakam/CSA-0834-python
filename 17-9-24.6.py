def reverse_number(num):
    num_str = ''.join(filter(str.isdigit, str(num))) 
    if num.startswith('-'):
        return '-' + num_str[::-1]  
    return num_str[::-1]  

num = input("Enter a number: ")
print("Reverse Number:", reverse_number(num))
