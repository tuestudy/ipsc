for _ in range(int(input())):
    input()
    tokens = input().strip().split()
    while len(tokens)>=3:
        a, op, b = tokens[:3]
        tokens = [str(int(eval('%s %s %s' % (a, op, b))))]+tokens[3:]
    print(tokens[0])
