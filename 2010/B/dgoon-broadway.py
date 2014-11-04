# /usr/bin/env python3
import math
T = int(input())

def calc_y(x, R, P, Q):
    return (R-P*x)/Q

def calc_x(y, R, P, Q):
    return (R-Q*y)/P

def inside(Ax, Ay, Bx, By, p):
    return (min(Ax, Bx) <= p[0] <= max(Ax, Bx)) and (min(Ay, By) <= p[1] <= max(Ay, By))

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

for _ in range(T):
    input()
    in_nums = input().strip().split()
    Ax, Ay, Bx, By = map(float, in_nums[:4])
    P, Q, R = map(float, in_nums[4:])

    length_without_broadway = abs(Ax-Bx) + abs(Ay-By)
    if Ax==Bx or Ay==By:
        print(length_without_broadway)
    elif P==0.0 or Q==0.0 or ((Bx-Ax)*(By-Ay))*(P*Q)>0.0:
        print(length_without_broadway)
    else:
        p0 = Ax, calc_y(Ax, R, P, Q)
        p1 = Bx, calc_y(Bx, R, P, Q)
        p2 = calc_x(Ay, R, P, Q), Ay
        p3 = calc_x(By, R, P, Q), By
        ps = set([x for x in [p0, p1, p2, p3] if inside(Ax, Ay, Bx, By, x)])
        if len(ps) < 2:
            print(length_without_broadway)
        else:
            l, r = sorted(ps)
            ll, rr = sorted([(Ax, Ay), (Bx, By)])
            length_with_broadway = dist(ll, l) + dist(l, r) + dist(r, rr)
            print(length_with_broadway)
