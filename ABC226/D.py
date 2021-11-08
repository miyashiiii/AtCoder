"""
https://atcoder.jp/contests/abc226/tasks/abc226_d

入力例
3
1 2
3 6
7 4

"""
import math


def main():
    n = int(input())

    towns = []
    magics = set()
    for i in range(n):
        towns.append(list(map(int, input().split())))

    for t1 in towns:
        for t2 in towns:
            if t1 != t2:
                a = t1[0] - t2[0]
                b = t1[1] - t2[1]
                gcd_ = math.gcd(a, b)
                magics.add((a // gcd_, b // gcd_))

    # print(magics)
    print(len(magics))


if __name__ == "__main__":
    main()
