#-*- encoding: utf-8
# /usr/bin/env python3
for _ in range(int(input())):
    input()
    input()
    Ns = [(int(n), idx+1) for idx, n in enumerate(input().strip().split())]
    s = sum(n for (n, _) in Ns)
    half_s = s/2
    first_ship = []
    fsum = 0
    second_ship = []
    ssum = 0

    target = 0
    for n, idx in Ns:
        if fsum<=ssum:
            if fsum+n>half_s:
                continue
            first_ship.append(idx)
            fsum += n
        else:
            if ssum+n>half_s:
                continue
            second_ship.append(idx)
            ssum += n
    print('%d %s' % (len(first_ship), ' '.join(str(x) for x in first_ship)))
    print('%d %s' % (len(second_ship), ' '.join(str(x) for x in second_ship)))
