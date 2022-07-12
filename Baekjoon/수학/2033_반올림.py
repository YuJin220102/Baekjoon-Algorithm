s = list(input())
ss = s[::-1]
count = 0

while(True):
    if(count >= len(ss) - 1) : break
    if(int(ss[count]) >= 5):
        ss[count] = '0'
        ss[count + 1] = str(int(ss[count + 1]) + 1)
    else:
        ss[count] = '0'
    count += 1
    
print(int(''.join(ss[::-1])))
