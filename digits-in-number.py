number = int( input())
count = 0
number = abs( number)
while number > 0:
    count = count + 1
    number = number // 10
print(count)