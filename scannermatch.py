#!/usr/bin/env python
#coding:utf8
def generate_tokens(pat,text):
Token = namedtuple('Token',['type','value'])
scanner = pat.scanner(text)
    for m in iter(scanner.match,None):
        yield Token(m.lastgroup,m.group())
for tok in generate_tokens(master_pat,'foo = 42'):
    print(tok)

