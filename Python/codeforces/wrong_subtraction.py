number, computations=map(int, input().split())
for i in range(computations):
    if number%10:
        number-=1
    else:
        number=number//10
print(number)
