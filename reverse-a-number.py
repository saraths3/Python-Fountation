number = int( input())
reverse = 0
negative = False
if number < 0:
    negative = True
    number = abs(number)
while number > 0:
    reminder = number % 10
    reverse = 10 * (reverse + reminder)
    number = number // 10
if negative:
    print((reverse - reverse * 2) // 10)
else:
    print(reverse // 10)