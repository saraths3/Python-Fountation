number = int( input())
sum = 0
negative = False
if number < 0:
    number = abs( number)
    negative = True
while number > 0:
    reminder = number % 10
    first = number
    sum = sum + reminder
    number = number // 10
if negative:
    print(sum - 1)
else:
    print(sum)