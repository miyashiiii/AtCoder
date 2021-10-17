"""
https://atcoder.jp/contests/abc213/tasks/abc213_c
4 5 2
3 2
2 5
"""
import numpy as np

_, _, n = input().split()
x_list = []
y_list = []
for i in range(int(n)):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
x_unique_ordered = list(set(x_list))
x_unique_ordered.sort()
y_unique_ordered = list(set(y_list))
y_unique_ordered.sort()

for x, y in zip(x_list,y_list):
    print(x_unique_ordered.index(x) + 1, y_unique_ordered.index(y) + 1)


