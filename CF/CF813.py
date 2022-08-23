def wonderfulperm():
    t = input()
    def minsum(k,inp):
        so = sorted(inp)
        reqar = so[0:k]
        numop =0
        for x in range(len(reqar)):
            val = reqar[x]
            ini = inp[x]
            if ini!= val:
                numop +=1
                inp[x] = val
                inp[inp.index(val)] = ini
        return numop

    inp = []
    kva =[]
    for i in range(int(t)):
        n,k = input().split()
        inp.append(list(map(int,input().split())))
        kva.append(int(k))

    for _ in range(int(t)):
        print(minsum(kva[_],inp[_]))

'''
t = int(input())
inp =[]
for i in range(t):
    n = input()
    inp.append(list(map(int,input().split())))

def minop(jusl):
    x = 2
    zerol = [0 if item==x else item for item in jusl]
    return zerol

#for i in range(t):
#    print(minop(n[i],inp[i]))
'''

wonderfulperm()

