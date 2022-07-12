while(True):
    s = input()
    if(s == '0') : break
    if(s[::-1] == s):
        print("yes")
    else:
        print("no")
