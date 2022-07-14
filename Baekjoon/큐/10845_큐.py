import sys
a = int(sys.stdin.readline())
queue = []

for i in range(a):
    b = sys.stdin.readline().split()
    if(b[0] == "push"):
        queue.append(b[1])
    elif(b[0] == "pop"):
        if(len(queue) == 0):
            print("-1")
        else:
            print(queue.pop(0))
    elif(b[0] == "size"):
        print(len(queue))
    elif(b[0] == "empty"):
        if(len(queue) == 0):
            print("1")
        else:
            print("0")
    elif(b[0] == "front"):
        if(len(queue) == 0):
            print("-1")
        else:
            print(queue[0])
    elif(b[0] == "back"):
        if(len(queue) == 0):
            print("-1")
        else:
            print(queue[len(queue) - 1])
            


