a, b = map(int, input().split())
num = 0
count = 0

for i in range(1, 1000):
    for j in range(0, i):
        count += 1
        if(count >= a and count <= b) :
            num += i
print(num)
