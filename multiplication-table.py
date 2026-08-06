list = list(map(int, input().split()))
for i in range(1, list[0] + 1):
    print(f'{i} x {list[1]} = {i * list[1]}')