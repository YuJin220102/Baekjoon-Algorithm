import math

num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    print(math.factorial(b) // (math.factorial(a) * math.factorial(b - a)))
