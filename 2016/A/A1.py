# -*- encoding: utf-8 -*-

from sys import stdin

N = 42

def solve(line):
    words = line.split()
    word_set = set(words)

    result = ''.join(list(word_set))
    n = len(result)
    if n < N:
        return result + 'A' * (N - n) 
    return ''.join(list(word_set))
    

if __name__ == "__main__":
    # ignore the number of test case
    stdin.readline()

    for line in stdin:
        line = line.strip()
        if len(line) > 0:
            result = solve(line)
            print(result)
            
    
