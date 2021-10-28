"""
https://atcoder.jp/contests/abc224/tasks/abc224_c

入力例
4
0 1
1 3
1 1
-1 -1

"""

import itertools


def main():
    ans = 0
    for (x1, y1), (x2, y2), (x3, y3) in itertools.combinations([[int(v) for v in input().split()] for i in range(int(input()))], 3):
        xdiff1 = (x1 - x2)
        xdiff2 = (x2 - x3)
        if xdiff1 == 0:
            grad1 = None
        else:
            grad1 = (y1 - y2) / xdiff1

        if xdiff2 == 0:
            grad2 = None
        else:
            grad2 = (y2 - y3) / xdiff2

        if grad1 != grad2:
            ans += 1
        # else:
        # print("--")
        # print(x1, y1)
        # print(x2, y2, grad1)
        # print(x3, y3, grad2)

    print(ans)


if __name__ == "__main__":
    main()
