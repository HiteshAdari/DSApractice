t = int(input())


def hashm(lis):
    x = {}
    for ele in lis:
        if ele in x:
            x[ele] += 1
        else:
            x[ele] = 1
    return x


def eqdis(lis, n):
    switch = 1
    b = []
    c = []
    has = hashm(lis)
    if len(has)%2 == 0:
        return True
    else:
        for ele in has:
            if has[ele]%2 ==0:
                return True
        return False
    '''
    for ele in has:
        if has[ele] % 2 == 0:
            #for i in range(int(has[ele] / 2)):
            b.append(ele)
            c.append(ele)
            has[ele] = 0
        elif has[ele] == 1:
            if switch == 1:
                b.append(ele)
                switch = 0
            else:
                c.append(ele)
                switch = 1
            has[ele] = 0
        elif has[ele] / 2 > 1:
            #for i in range(has[ele] // 2):
            b.append(ele)
            c.append(ele)
            has[ele] = 0
    '''
    '''    for ele in has:
        if has[ele] == 1:
            if switch == 1:
                b.append(ele)
                switch = 0
            else:
                c.append(ele)
                switch = 1
    '''
    '''
    if len(hashm(b)) == len(hashm(c)):
        return True
    else:
        return False
    '''

arr = []
n = []
for i in range(t):
    n.append(int(input()))
    arr.append(list(map(int, input().split())))

for i in range(t):
    if eqdis(arr[i], n[i]):
        print('YES')
    else:
        print('NO')
