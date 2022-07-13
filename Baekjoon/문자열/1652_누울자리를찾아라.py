a = int(input())
board = [list(input()) for _ in range(a)]
r, c = 0, 0

for i in range(a):
    cut, cut2 = 0, 0
    for j in range(a):
        #가로
        if(board[i][j] == '.'):
            cut += 1
            if(cut == 2) :
                r += 1
        elif(board[i][j] == 'X'):
            cut = 0
        #세로
        if(board[j][i] == '.'):
            cut2 += 1
            if(cut2 == 2) :
                c += 1
        elif(board[j][i] == 'X'):
            cut2 = 0
        
print(r, c)
