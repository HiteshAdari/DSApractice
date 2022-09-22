def gcdlcm():
    import math
    t = int(input())
    ans = []

    def eq(lis):
        has = {}
        for el in lis:
            if el in has:
                has[el] += 1
            else:
                has[el] = 1
        total = 0
        for x in has:
            if has[x] > 1:
                total += (math.factorial(has[x]) * math.factorial(has[x] - 2)) / 2
        return total

    for i in range(t):
        n = int(input())
        lis = list(map(int, input().split()))
        ans.append(eq(lis))
    for an in ans:
        print(an)


def interestingsubarr():
    t = int(input())
    ans = []

    def prod(lis):
        ma = max(lis)
        mi = min(lis)
        return min(mi * mi, ma * mi), max(ma * ma, mi * mi)

    for i in range(t):
        n = int(input())
        lis = list(map(int, input().split()))
        x, y = prod(lis)
        ans.append([x, y])

    for el in ans:
        print(el[0], end=' ')
        print(el[1])


def pokemonbattles():
    t = int(input())
    ans = []

    def maxscr(gr, wa, n):
        scrg = [0] * n
        scrw = [0] * n
        hasg = {}
        hasw = {}
        for i in range(n):
            hasg[gr[i]] = i
            hasw[wa[i]] = i
        sogr = sorted(gr)
        sowa = sorted(wa)
        for i in range(n):
            scrg[hasg[sogr[i]]] += i
            scrw[hasw[sowa[i]]] += i
        scr = []
        for i in range(n):
            scr.append(scrw[i] + scrg[i])
        total = 0
        mag = max(scrg)
        maw = max(scrw)
        ma = max(scr)
        for i in range(n):
            if scrg[i] == mag or scrw[i] == maw or scr[i] == ma:
                total +=1
        return total

    for i in range(t):
        n = int(input())
        ground = list(map(int, input().split()))
        water = list(map(int, input().split()))
        ans.append(maxscr(ground, water, n))

    for an in ans:
        print(an)


def alonealice():
    n = int(input())
    s = input()
    q = int(input())
    for i in range(q):
        l, r = input().split()

import math
a, b = input().split()
a, b = int(a), int(b)
zero2 = 1
zero5 = 1
for i in range(a + 1, b + 1):
    zero2 = zero2*int(math.log(i,2))
    if i >5:
        zero5 = zero5*int(math.log(i,5))

print(min(zero5, zero2)%(10**9+7))
