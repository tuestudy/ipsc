def to_base(n, b):
    r = []
    while n!=0:
        a = n%b
        if a>=10:
            a = chr(ord('a')+(a-10))
        r.append(str(a))
        n = int(n / b)
    return ''.join(reversed(r))

def is_good(t, b, k):
    tb = to_base(t, b)
    #print('%s -> %s' % (t, tb))
    shifted_tb = tb[-1] + tb[:-1]
    #print('shifted: %s' % shifted_tb)
    if t == int(shifted_tb, b)*k:
        return True
    return False

for _ in range(input()):
    raw_input()
    b, k = map(int, raw_input().strip().split())

    if k==1:
        print('2 1')
        continue

    if k>b:
        print('NO')
        continue

    if k==b:
        print('2 1')
        continue

    t = 10
    bb = b**b
    while True:
        if is_good(t, b, k):
            break
        if t>=bb:
            t = -1
            break
        t += 1

    if t>=0:
        tb = to_base(t, b)
        print('%s %s' % (len(str(tb)), int(tb[0], b)))
    else:
        print('NO')
