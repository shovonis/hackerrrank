#!/usr/bin/env python

_author_ = "rifatul.islam"

dim = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
tmp_list = []

for i in range(0, dim[1]):
    tmp_list.append(arr[i])

del arr[:dim[1]]

for i in tmp_list:
    arr.append(i)

for x in arr:
    print(x, end=" ")