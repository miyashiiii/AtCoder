"""
https://atcoder.jp/contests/abc215/tasks/abc215_c

aab 2

"""
import itertools


def main():
    s, k = input().split()
    l = list(set((itertools.permutations(s))))
    l.sort()
    print("".join(l[int(k) - 1]))


if __name__ == "__main__":
    main()
