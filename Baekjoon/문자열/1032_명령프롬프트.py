a = int(input())
str = list(input())

for i in range(a - 1):
    b = list(input())
    for j in range(len(str)):
        if(str[j] != b[j]):
            str[j] = '?'
print(''.join(str))
