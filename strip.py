#1/usr/bin/env python
#coding:utf8
with open(somefile.py) as f:
    lines=(line.strp() for line in f)
    for line in lines:
        print(line)
