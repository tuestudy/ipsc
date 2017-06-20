# -*- encoding: utf-8 -*-

from sys import stdin

N = 39

def is_overlapped(s1, s2):
    n = len(s1)
    for i in reversed(range(n)):
        sub = s1[i:n]
        if sub == s2[:n - i]:
            return True
    n = len(s2)
    for i in reversed(range(n)):
        sub = s2[i:n]
        if sub == s1[:n - i]:
            return True
    return False

def combine_words(s1, s2):
    n = len(s1)
    for i in reversed(range(n)):
        sub = s1[i:n]
        if sub == s2[:n - i]:
            return s1[:i] + s2
    n = len(s2)
    for i in reversed(range(n)):
        sub = s2[i:n]
        if sub == s1[:n - i]:
            return s2[:i] + s1
    return s1 + s2

def solve2(line):
    words = list(set(line.split()))
    wc = len(words)
    found = False
    for i in range(wc - 1):
        for j in range(i + 1, wc):
            s = combine_words(words[i], words[j])
            if len(s) < 8:
                pair = (words[i], words[j])
                found = True
                break
        if found:
            break

    if found:
        s1, s2 = pair
        words.remove(s1)
        words.remove(s2)
        words.append(s)

    result = ''.join(words)
    n = len(result)
    if n < N:
        return result + 'A' * (N - n)
    return result


if __name__ == "__main__":
    # ignore the number of test case
    stdin.readline()

    for line in stdin:
        line = line.strip()

        if len(line) == 0:
            continue

        result = solve2(line)
        if len(result) == N:
            print(result)
