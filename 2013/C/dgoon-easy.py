import math
import sympy
import sys

def t(n):
    z=n
    factors = sympy.factorint(n).keys()
    for a in factors:  #range(2,int(math.sqrt(n))):
        if n%a==0: z//=a ; z*=a-1
    return min(z+1,n)

def run(A):
    orig_A = A[:]
    A.sort()
    for i in xrange(4): A[i+5] ^= t(A[i+1]-A[0])>>7
    z = max( t(A[0])-1, A[0]+1-t(A[0]) )
    s = z%len(A)
    for i in xrange(s): A = A[1:] + A[:1]
    A.insert(1,z)
    r = []
    for x in range(8,10**7):
        y = A[x//4]>>(18-6*(x%4))&63
        if y: r.append(str(chr(31+y) if y<60 else A[y-60]))
        else: break
    r = ''.join(r)
    rs = r.split()
    if rs[0]=='CHANGE':
        orig_A[orig_A.index(int(rs[1]))] = int(rs[3])
        return run(orig_A)
    else:
        return r

A = [ 1894607624, 1927505134, 1861486949, 2052221263, 1953703270, 1772249212, 1704106159, 1607055075, 1829198849 ]
print run(A)
