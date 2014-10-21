import numpy as np
from collections import defaultdict

ingredients = ['milk', 'egg', 'sugar', 'salt', 'flour']
fillings = ['banana', 'strawberry jam', 'chocolate', 'walnut']
cake_ingredients = np.array([8.0, 8.0, 4.0, 1.0, 9.0])
cake_fillings = {
        'banana': [1, 0, 0, 0],
        'strawberry': [0, 30, 0, 0],
        'chocolate': [0, 0, 25, 0],
        'walnut': [0, 0, 0, 10],
}

def is_I_good(I):
    for i in I:
        if i<0.0:
            return False
    return True

for _ in range(input()):
    raw_input()
    I = np.array(map(float, raw_input().strip().split()))
    F = np.array(map(float, raw_input().strip().split()))
    MAX = int(min(I/cake_ingredients)*16)

    b = int(F[0]/cake_fillings['banana'][0])
    s = int(F[1]/cake_fillings['strawberry'][1])
    c = int(F[2]/cake_fillings['chocolate'][2])
    w = int(F[3]/cake_fillings['walnut'][3])
    print(min(MAX, b+s+c+w))
