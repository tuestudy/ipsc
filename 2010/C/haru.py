def evaluate(lookup, exps):
    for k, v in exps.iteritems():
        tokens = []
        for t in v:
            if t in lookup:
                tokens.append(str(lookup[t]))
            else:
                tokens.append(t)
        try:
            lookup[k] = eval(''.join(tokens))
            del exps[k]
            return
        except NameError:
            pass

def main():
    t = input()

    for i in range(t):
        if i > 0:
            print 
        raw_input()
        n = input()
        exps = {}
        for i in range(n):
            key, exp = raw_input().strip().split(' = ')
            exps[key] = exp.split()

        result = {}
        while not len(exps) == 0:
            evaluate(result, exps)

        keys = sorted(result.keys())
        for k in sorted(result.keys()):
            print '{} = {}'.format(k, result[k])

if __name__ == '__main__':
    main()
