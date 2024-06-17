def is_palindrome(string):
    str_num = str(string)
    return str_num == str_num[::-1]
string = str(input("Enter a number: "))
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
