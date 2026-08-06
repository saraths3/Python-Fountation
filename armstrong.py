def armstrong(n):
    value = 0
    digit_length = len(str(n))
    while n > 0:
        reminder = n % 10
        value = value + (reminder ** digit_length)
        n = n // 10
    if value == number:
        return True
number = int( input())
if number >= 0:
    print(armstrong(number))