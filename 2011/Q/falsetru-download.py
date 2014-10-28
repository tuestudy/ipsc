from contextlib import closing
import time
import urllib

for i in range(1, 1000):
    print i
    with closing(urllib.urlopen('http://ipsc.ksp.sk/2011/practice/problems/q.html')) as u:
        with open('{}.html'.format(i), 'wb') as f:
            f.write(u.read())
    time.sleep(10)
