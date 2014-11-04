T = input()
for i in range(T):
    raw_input()
    A = input()
    delta = 2 if i % 2 == A % 2 else 1
    if A > 999000000: delta *= -1
    B = A + delta
    print B
