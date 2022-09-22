def A():
    t = input()
    frac = []
    for _ in range(int(t)):
        frac.append(list(map(int, input().split())))
    ans = []
    for f in frac:
        a, b, c, d = f[0], f[1], f[2], f[3]
        f1 = a / b
        f2 = c / d
        if f1 == f2:
            ans.append(0)
        else:
            x = a * d
            y = c * b
            if x==0 or y==0:
                ans.append(1)
            elif x / y > 1:
                if x / y == x // y:
                    ans.append(1)
                else:
                    ans.append(2)
            elif x/y <1:
                if y/x == y//x:ans.append(1)
                else:ans.append(2)
    for a in ans:
        print(a)

def B():
    t = int(input())
    n = []
    ar=[]
    ans=[]
    for _ in range(t):
        n.append(int(input()))

        ar.append(list(map(int, input().split())))

A()
