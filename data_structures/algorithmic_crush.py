#!/usr/bin/env python

_author_ = "rifatul.islam"

arr = []
n, m = [int(arr_temp) for arr_temp in input().strip().split(' ')]

zList = [0] * (n+1)
max = 0
x = 0
for i in range(m):
    a, b, k = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    zList[a - 1] += k
    if b <= len(zList):
        zList[b] -= k
    print(zList)

for i in zList:
    x = x + i
    if max < x:
        max = x

print(max)
