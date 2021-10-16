"""
https://atcoder.jp/contests/abc221/tasks/abc221_c入力例
998244353

"""
import itertools

l = [int(c) for c in input()]
l.sort(reverse=True)

idx_list = list(range(len(l)))
c = itertools.combinations(idx_list, len(l) // 2)

max_ = 0
for indexes1 in c:
    indexes2 = set(idx_list) - set(indexes1)
    n1 = int("".join([str(l[i]) for i in indexes1]))
    n2 = int("".join([str(l[i]) for i in indexes2]))
    pd = n1 * n2
    if max_ < pd:
        max_ = pd

print(max_)
