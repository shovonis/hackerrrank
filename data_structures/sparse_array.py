#!/usr/bin/env python

_author_ = "rifatul.islam"

strings = []
queries = []

n = int(input().strip())
for i in range(n):
    strings.append(input().strip())

q = int(input().strip())
for i in range(q):
    queries.append(input().strip())

for q in queries:
    count = 0
    for str in strings:
        if q == str:
            count += 1
    print(count)
