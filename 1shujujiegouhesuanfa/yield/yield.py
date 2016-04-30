#!/usr/bin/env python
#coding:utf8
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
nested = [[1,2],[3,4],[5,6]]
for num in flatten(nested):
    print num,
