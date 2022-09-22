
def chipgame():
    t = input()
    x = []
    for i in range(int(t)):
        n, m = input().split()
        n, m = int(n), int(m)
        if (n % 2 == 0 and m % 2 == 0) or (n % 2 == 1 and m % 2 == 1):
            x.append('Tonya')
        else:
            x.append('Burenka')

    for win in x:
        print(win)


def mathcircus():
    n, k = 4, 1
    '''
    lisn = [i for i in range(1,n+1)]
    ans = []
    for i in range(1,n+1):
        if i in lisn:
            x = lisn[0]
            l=0
            while (((i+k)*(x))%4 !=0) and l<len(lisn):
                l +=1
                x = lisn[l]
            if (((i+k)*(x))%4 ==0):
                ans.append((i,x))
                lisn.remove(x)
                lisn.remove(i)
    
    print(ans)
    '''


def fightingtourney():
    import copy
    t = input()
    ans = []
    for i in range(int(t)):
        n, q = input().split()
        n, q = int(n), int(q)

        inia = list(map(int, input().split()))
        inid = [i for i in range(1, n + 1)]

        que = []
        for _ in range(q):
            que.append([int(x) for x in input().split()])

        for val in que:
            a = copy.deepcopy(inia)
            id = copy.deepcopy(inid)
            i, k = val[0], val[1]
            x = 1
            wins = 0
            while x <= k:
                oppo1 = id[0]
                oppo2 = id[1]
                val1 = a[0]
                val2 = a[1]

                if val1 > val2:
                    id.remove(oppo2)
                    id.append(oppo2)
                    a.remove(val2)
                    a.append(val2)
                    if oppo1 == i:
                        wins += 1
                else:
                    id.remove(oppo1)
                    id.append(oppo1)
                    a.remove(val1)
                    a.append(val1)
                    if oppo2 == i:
                        wins += 1
                x += 1
            ans.append(wins)

    for numw in ans:
        print(numw)


