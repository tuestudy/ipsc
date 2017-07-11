#!/usr/bin/env python

# required requests and beautifulsoup4
#   pip install requests
#   pip install beautifulsoup4

import os
import sys
import re
import pickle
import requests, requests.utils
from bs4 import BeautifulSoup

class IPSC(object):
    def __init__(self, problem):
        self.problem = problem.upper() if problem != None else problem
        self.cookiefile_path = os.path.join(os.path.expanduser('~'), '.ipsccj')
        self.session = requests.Session()
        self.has_cookie = False
        try:
            with open(self.cookiefile_path, 'rb') as f:
                cookies = requests.utils.cookiejar_from_dict(pickle.load(f))
                self.session.cookies = cookies
                self.has_cookie = True
        except IOError:
            print('IOError')
            pass
        except Exception as e:
            import traceback
            traceback.print_exc()

    def submit(self, filepath):
        problem = 'ipsc{0[0]}.{0[1]}'.format(self.problem.split('/'))
        url = 'https://ipsc.ksp.sk/train/submit'
        r = self.session.post(url, { 'dis': problem }, files={ 'output_file': open(filepath, 'rb') })
        if not self.has_cookie:
            with open(self.cookiefile_path, 'wb') as f:
                pickle.dump(requests.utils.dict_from_cookiejar(self.session.cookies), f)

    def show_submission_history(self):
        url = 'https://ipsc.ksp.sk/train/submit'
        r = self.session.get(url)
        soup = BeautifulSoup(r.text.encode('utf-8'), 'html.parser')
        submit_rows = soup.find_all('tr', class_=re.compile('submit-.*'))
        for row in submit_rows:
            date, name, result, _ = row.find_all('td')
            if not self.problem or name.text == self.problem:
                print('{}\t{}\t{}'.format(date.text, name.text, result.text))

def submit(problem, filepath):
    site = IPSC(problem)
    site.submit(filepath)
    site.show_submission_history()

def history(problem):
    IPSC(problem).show_submission_history()

def usage(cmd):
    print('Usage  : {} <subcmd> [<problem> <file>]'.format(cmd))
    print('    subcmd: submit or history')
    print('    problem: {year}/{num}. e.g. 2014/A1')

def main(cmd, subcmd=None, problem=None, filepath=None):
    if subcmd == 'submit' and problem != None and filepath != None:
        submit(problem, filepath)
        return

    if subcmd == 'history':
        history(problem)
        return

    usage(cmd)

if __name__ == '__main__':
    main(*sys.argv)
