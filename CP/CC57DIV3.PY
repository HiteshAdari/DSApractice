def non_neg():
    t = int(input())
    ans = []
    def odd(lis):
        count = 0
        for num in lis:
            if num < 0:
                count += 1
            elif num == 0:
                return 0
        if count%2 == 0:
            return 0
        else:
            return 1
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().split()))
        ans.append(odd(A))
    for an in ans:
        print(an)
def even_splits():
    t = int(input())
    ans = []
    def ret(s):
        if len(s) <=2:
            return s
        count0 = 0
        count1 = 0
        for c in s:

            if c == '0':
                count0 += 1
            else:
                count1 += 1
        ans = ''
        if count0 > 0:
            for i in range(count0):
                ans += '0'
            for i in range(count1):
                ans += '1'
        else:
            return s
        return ans
    for _ in range(t):
        n = int(input())
        s = input()
        ans.append(ret(s))

    for an in ans:
        print(an)
def twodiffpalind():
    t = int(input())
    ans = []
    def ret(a,b):
        if a==0  or b == 0:
            return 'NO'
        elif a%2 ==0 and b%2 == 0:
            return 'YES'
        elif a%2 == 1 and b%2 == 1:
            return 'NO'
        elif a%2 == 1:
            if a > 1:
                return 'YES'
            else:
                return 'NO'
        else:
            if b > 1:
                return 'YES'
            else:
                return 'NO'
    for _ in range(t):
        A,B = input().split()
        ans.append(ret(int(A),int(B)))

    for an in ans:
        print(an)
def maxexpr():
    t = int(input())
    ans = []

    def maxform(s):
        l = len(s)
        stk = []
        numpl = 0
        nummi = 0
        for char in s:
            if char == '+':
                numpl += 1
            elif char == '-':
                nummi += 1
            else:
                stk.append(int(char))
        stk = sorted(stk)
        ans = ''
        for _ in range(len(stk)-numpl-nummi):
            ans += str(stk.pop())
        for _ in range(numpl):
            ans += '+'
            ans += str(stk.pop())
        for _ in range(nummi):
            ans += '-'
            ans += str(stk.pop())

        return ans
    for i in range(t):
        n = int(input())
        s = input()
        ans.append(maxform(s))
    for an in ans:
        print(an)


t = int(input())
ans = []
def delic(m,p,k):
    stk = []
    has = set()
    for i,num in enumerate(m):
        if num%p == 0:
            has.add(i)
            stk.append(num)

    delica = 0
    if min(has) >=k:
        for j in range(k):
            delica += m[j]
    else:
        stk = sorted(stk)
        for j in range(k):
            if j in has:
                delica += stk.pop()
            else:delica += m[j]
    return delica
for _ in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        p,k = map(int, input().split())
        ans.append(delic(m,p,k))
for an in ans:
    print(an)
