#!/usr/bin/env python
#coding:utf8
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
for num in flatten([[1,2,3],2,4,[5,[6],7]]):
    print num
