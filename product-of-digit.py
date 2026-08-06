number = int( input())
negative = False
product_ = 1
if number < 0:
    number = abs(number)
    negative = True
while number > 0:
    reminder = number % 10
    product_ = product_ * reminder
    number = number // 10
if negative:
    print(-abs(product_))
else:
    print(product_)