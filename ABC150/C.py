"""
https://atcoder.jp/contests/abc150/tasks/abc150_c

3
1 3 2
3 1 2


"""

import itertools


def main():
    n = int(input())
    pattern = list(itertools.permutations(range(1, n + 1)))
    # print(pattern)
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    print(abs(pattern.index(p) - pattern.index(q)))


if __name__ == "__main__":
    main()
