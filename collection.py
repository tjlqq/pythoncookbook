#1/usr/bin/env python
#coding:utf8
from collections import deque

def search(lines, pattern,history=10):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)
if __name__ == '__main__':
    with open(r'somefile.txt') as f:
        for line,prevlines in search(f,'python',5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('_' * 20)
