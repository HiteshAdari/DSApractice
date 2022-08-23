n = 8

bo = [[-1 for i in range(n)]for i in range(n)]

movei = [1,2,-1,-2,1,-1,2,-2]
movej = [2,1,-2,-1,-2,2,-1,1]


def isavail(a,b,bo):
    if a>=0 and b>=0 and a<n and b<n and bo[a][b] ==-1:
        return True
    else:
        return False

def sol(n,board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def meth(movei,movej,bo):
    count =1
    newx,newy =0,0
    for i in range(len(movei)):
        newx += movei[i]
        newy += movej[i]
        if isavail(newx,newy,bo):
            count +=1
            bo[newx][newy] = count

meth(movei,movej,bo)
sol(n,bo)



