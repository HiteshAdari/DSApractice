input1 = int(input())
input2 = input()

r = input2

b = ''
k = ''


while len(k) != input1:
    R = len(r)
    B = len(b)
    if B ==0:
        b = b + r[0]
        r = r[1:]
    elif R ==0:
        k = b[-1] + k
        b = b[:B-1]
    else:
        if r[0] > b[-1]:
            b = b + r[0]
            r = r[1:]
        elif r[0] < b[-1]:
            k = b[-1] + k
            b = b[:B - 1]

print(k)
