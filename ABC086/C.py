"""
(AtCoder Beginners Selection)
https://atcoder.jp/contests/abs/tasks/arc089_a

2
3 1 2
6 1 1
"""

n = int(input())

before_t, before_x, before_y = 0, 0, 0
for i in range(n):
    t, x, y = [int(c) for c in input().split()]
    tmp_t = t - before_t
    move_x = abs(x - before_x)
    move_y = abs(y - before_y)
    move = move_x + move_y

    if tmp_t < move:
        print("No")
        exit()

    if move % 2 != tmp_t % 2:
        print("No")
        exit()
    before_x = x
    before_y = y
    before_t = t

print("Yes")
