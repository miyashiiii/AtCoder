"""
https://atcoder.jp/contests/abc221/tasks/abc221_c入力例
998244353

"""
import itertools

l = list(input())
p = itertools.permutations(l)
max_num = 0
for v in p:
    for i in range(len(l)):
        if i in [0, len(l) - 1]:
            continue

        n1 = int("".join(v[:i]))
        n2 = int("".join(v[i:]))

        product = n1 * n2
        # print(product)
        if product > max_num:
            max_num = product

print(max_num)
