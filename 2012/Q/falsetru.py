from collections import defaultdict, Counter
import itertools
import string


def structure(word):
    """
    >>> structure('kitty')
    (0, 1, 2, 2, 3)
    """
    d = defaultdict(itertools.count().next)
    return tuple(d[c] for c in word)


def group_words(words):
    groups = defaultdict(list)
    for w in words:
        groups[structure(w)].append(w)

    for s in sorted(groups, key=lambda k: (len(groups[k]), k)):
        yield groups[s]


def solve(wordlist1, wordlist2, known=None):
    if known is None:
        known = {}
    words_pairs = zip(*map(group_words, (wordlist1, wordlist2)))
    for try_cnt in range(10):
        # 1. By frequency
        c1 = Counter(c for a, b in words_pairs for w in a for c in w)
        c2 = Counter(c for a, b in words_pairs for w in b for c in w)
        d1, d2 = defaultdict(list), defaultdict(list)
        for k, v in c1.items():
            d1[v].append(k)
        for k, v in c2.items():
            d2[v].append(k)
        for k, v in d1.items():
            if len(v) == 1:
                known[v[0]] = d2[k][0]

        # 2. Remove words that contains known characters only
        for words1, words2 in words_pairs:
            to_remove = {word for word in words1
                         if all(x in known for x in word)}
            to_remove2 = {''.join(map(known.get, w)) for w in to_remove}
            words1[:] = [w for w in words1 if w not in to_remove]
            words2[:] = [w for w in words2 if w not in to_remove2]

        # 3. If only 1 pair; obvious
            if len(words1) == 1:
                known.update(dict(zip(words1[0], words2[0])))
        words_pairs = [xss for xss in words_pairs if len(xss[0]) > 1]
        if not words_pairs:
            break
    if try_cnt == 9:
        if len(words_pairs) == 1:
            k = solve1(words_pairs[0][0], words_pairs[0][1], known)
            if k:
                return k
        # XXX
        known = dict(zip('abcfghijlnopqrtuvwxz',
                         'wtsolufimgjvbchkyepq'))
        return solve(words_pairs[-1][0], words_pairs[-1][1], known)
    return known


def agree(known, w1, w2):
    known = known.copy()
    for a, b in zip(w1, w2):
        if a in known:
            if known[a] != b:
                return
        else:
            known[a] = b
    return known


def solve26(wordlist1, wordlist2):
    w1, w1s = wordlist1[0], wordlist1[1:]
    for i, w2 in enumerate(wordlist2):
        w2s = wordlist2[:i] + wordlist2[i + 1:]
        known = dict(zip(w1, w2))
        if all(''.join(known[c] for c in w) in w2s for w in w1s):
            return known


def solve1(w1s, w2s, known):
    if not w1s:
        return known
    for i, w1 in enumerate(w1s):
        w1r = w1s[:i] + w1s[i+1:]
        for j, w2 in enumerate(w2s):
            known2 = agree(known, w1, w2)
            if not known2:
                continue
            w2r = w2s[:j] + w2s[j+1:]
            k = solve1(w1r, w2r, known2)
            if k:
                return k

for _ in range(input()):
    raw_input()
    n = input()
    w1 = [raw_input() for _ in range(n)]
    w2 = [raw_input() for _ in range(n)]
    if all(len(w) == 26 for w in w1):
        known = solve26(w1, w2)
    else:
        known = solve(w1, w2)

    unknown = iter(sorted(set(string.ascii_lowercase) - set(known.values())))

    ret = ''.join(known[c] if c in known else next(unknown)
                  for c in string.ascii_lowercase)
    print ret
    assert set(Counter(ret).values()) == {1}


#solve(w1, w2)
