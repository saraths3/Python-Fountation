def palindrome(n):
    value = 0
    while n > 0:
        reminder = n % 10 
        value = 10 * (reminder + value)
        n = n // 10
    if (value // 10) == number:
        return True
number = int( input())
if number > 0:
    print(palindrome(number))