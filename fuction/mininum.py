#!/usr/bin/env python
#coding:utf8
def mininum(*values,clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip >m else m
    return m
print mininum(1,5,2,-5,10)
print mininum(1,5,2,-5,10,clip=0)
