def brokenphone():
    t = int(input())
    X = []
    Y = []
    for _ in range(t):
        x,y = input().split()
        X.append(int(x))
        Y.append(int(y))

    for i in range(t):
        x = X[i]
        y = Y[i]
        if x < y:
            print('REPAIR')
        elif x >y :
            print('NEW PHONE')
        else:
            print('ANY')


def permutationclear():
    t = int(input())
    ans = []
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        k = int(input())
        karr = set(map(int, input().split()))
        lis = []
        for el in arr:
            if el not in karr:
                lis.append(el)
        ans.append(lis)
    for ar in ans:
        for el in ar:
            print(el,end=' ')
        print('')


def mean_median():
    t = int(input())
    ans = []
    for _ in range(t):
        x,y = input().split()
        x = int(x)
        y = int(y)
        sum = 3*x-y

        if y > 0:
            if sum >y:
                ans.append([0,y,sum])
            else:
                ans.append([sum-y-1,y,y+1])
        else:
            if sum <y:
                ans.append([sum,y,0])
            else:
                ans.append([y-1,y,sum-y+1])
    for ar in ans:
        for el in ar:
            print(el,end=' ')
        print('')


def balls_boxes():
    t = int(input())
    ans = []
    for _ in range(t):
        x,y = input().split()
        n = int(x)
        k = int(y)
        ma = (k*(k+1))/2
        if ma <= n:
            ans.append('YES')
        else:
            ans.append('NO')

    for an in ans:
        print(an)

import math
def ball_seq():
    t = int(input())
    ans = []

    def dropped(n,lis):
        count = 0
        val = 0
        prev = 0
        for el in lis:
            num = el-prev-1
            prev = el

        return count
    for _ in range(t):
        x,y = input().split()
        n = int(x)
        k = int(y)
        type2 = list(map(int,input().split()))
        ans.append(dropped(n,type2))

    for el in ans:
        print(el)
