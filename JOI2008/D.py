"""
https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e

2 5
0 1 0 1 0
1 0 0 0 1

"""

import numpy as np


def main():
    r, c = map(int, input().split())

    senbeis = []
    for i in range(r):
        senbei_row = [not bool(int(i)) for i in input().split()]
        senbeis.append(senbei_row)
    senbeis = np.array(senbeis)
    # print(senbeis)
    # print()

    ans = 0
    for i in range(2 ** r):
        # print("i",bin(i))
        r_tmp_senbeis = senbeis.copy()
        # print(bin(i))
        for j in range(r):
            if (i >> j) & 1:
                r_tmp_senbeis[j, :] = np.logical_not(r_tmp_senbeis[j, :])

        count = 0
        for k in range(c):
            col_count = r_tmp_senbeis[:, k].sum()
            count += max(col_count, r - col_count)

        ans = max(ans, count)
    print(ans)


if __name__ == "__main__":
    main()
