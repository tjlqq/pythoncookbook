#!/usr/bin/env python
#coding:utf8
def simple_generator():
    yield 1
print simple_generator()
def repeater(value):
    while True:
        new = (yield value)
        print new
        print type(new)
        if new is not None:value = new
r = repeater(42)
print r.next()
print r.send('hello,world')
