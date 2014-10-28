from contextlib import closing
import time
import urllib

data = [list(' ' * 80) for i in range(60)]
for i in range(1, 2000):
    try:
        with open('{}.html'.format(i)) as f:
            content = f.read()
    except IOError:
        break

    lines = [line for line in content.splitlines()][6:66]
    for line, row in zip(lines, data):
        for i, c in enumerate(line):
            if not c.isspace():
                row[i] = c

for row in data:
    print(''.join(row).strip())
