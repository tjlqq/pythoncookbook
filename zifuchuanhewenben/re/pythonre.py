#!/usr/bin/env python
#coding:UTF-8
import re
pattern = re.compile(r'hello')
match = pattern.match('hello world!')
if match:
    print match.group()

