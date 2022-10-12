def car_Remov():
    t = int(input())
    def maxi(l):
        has = {}
        max = 0
        for el in l:
            if el not in has:
                has[el] = 1
            else:
                has[el] += 1
        for el in has:
            if has[el] > max:
                max = has[el]
        return max
    for i in range(t):
        n = int(input())
        lis = list(map(int,input().split()))
        print(n - maxi(lis))
def paper_cut():
    import math
    t = int(input())
    ans = []
    def nu(n,k):
        area = n*n
        ar = k*k
        l = int(math.sqrt(area/ar))
        return l*l
    for i in range(t):
        n,k = map(int, input().split())
        ans.append(nu(n,k))
    for an in ans:
        print(an)
def palin_rev():
    t = int(input())
    ans = []
    def foo(l,s):
        c0 = c1 =0
        for i in s:
            if i == '0':
                c0 += 1
            else:
                c1 += 1
        if c0 == 0 or c1 == 0:
            return True
        elif l%2 == 0 and l >=3:
            if c0%2 == 0:
                return True
            else:
                return False
        elif l%2 != 0 :
            return True
        else: return False

    for i in range(t):
        n =int(input())
        s = input()
        ans.append(foo(n,s))
    for an in ans:
        if an:
            print('YES')
        else:
            print('NO')
def yet_another_palin():
    t = int(input())
    ans = []
    def br(n,l):
        if l == l[::-1]:
            return 0

        if n%2 ==0:
            lef = int(n/2)
            rig = lef
            lef = lef-1
        else:
            lef = int(n//2)
            rig = lef+1
            lef = lef-1

        num = 0
        for i in range(int(n//2)):
            if l[lef]+num > l[rig]:
                return -1
            x = l[rig]-l[lef]-num
            num +=x
            lef -= 1
            rig += 1
        return num
    for i in range(t):
        n =int(input())
        lis = list(map(int,input().split()))
        ans.append(br(n,lis))

    for an in ans:
        print(an)
def distinct_num():
    t = int(input())
    ans = []
    def yea(n,k,l):
        has = set()
        a = 1
        x = 2*n
        score = 0
        for el in l:
            has.add(el)
        while k !=0:
            if max(has) <x:
                True
                #I dont know what to lul
        return score

    for i in range(t):
        n,k =map(int,input().split())
        lis = list(map(int,input().split()))
        ans.append(yea(n,k,lis))
    for an in ans:
        print(an)
