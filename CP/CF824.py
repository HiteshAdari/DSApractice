#incomplete

t = int(input())
ans = []
def giv(s):
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    has = {}
    let = set()
    i = 0
    ans = ''
    for c in s:
        if c not in has:
            if c == alph[i]:
                has[c] = alph[i+1]
                let.add(alph[i+1])

            else:
                has[c] = alph[i]
                let.add(alph[i])
                i += 1


    for c in s:
        ans += has[c]
    return ans
for u in range(t):
    n = int(input())
    stt = input()
    ans.append(giv(stt))
for an in ans:
    print(an)
