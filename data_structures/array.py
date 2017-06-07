#!/usr/bin/env python

_author_ = "rifatul.islam"

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]


rev_arr = []
i = 0
while n > 0:
    rev_arr.append(arr[n-1])
    n -= 1

for x in rev_arr:
    print(x, end=" ")