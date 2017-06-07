#!/usr/bin/env python
import sys

_author_ = "rifatul.islam"

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

sum_arr = -1000000
for i in range(6):
    for j in range(6):
        if (i + 2 < 6 and j + 2 < 6):
            temp_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][
                j + 1] + arr[i + 2][j + 2]
        if (temp_sum > sum_arr):
            sum_arr = temp_sum

print(sum_arr)
