"""
https://atcoder.jp/contests/abc145/tasks/abc145_c

3
0 0
1 0
0 1

"""

import itertools
import math


def main():
    n = int(input())

    towns = []
    for i in range(n):
        towns.append(list(map(int, input().split())))

    p = itertools.permutations(towns)

    total_distance = 0
    for route in p:
        for i in range(len(route) - 1):
            x1, y1 = route[i]
            x2, y2 = route[i + 1]
            total_distance += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    print(total_distance / math.factorial(n))


if __name__ == "__main__":
    main()
