"""
https://atcoder.jp/contests/abc128/tasks/abc128_c

2 2
2 1 2
1 2
0 1

"""


def main():
    n, m = map(int, input().split())
    bulbs = []
    for i in range(m):
        switches = [int(i) - 1 for i in input().split()]
        bulbs.append(switches[1:])

    p = list(map(int, input().split()))
    ans = 0

    for i in range(2 ** n):
        # print(bin(i))
        for bulb in range(m):
            switches_count = 0
            for j in range(n):
                # 順に右にシフトさせ最下位bitのチェックを行う
                if (i >> j) & 1:
                    if j in bulbs[bulb]:
                        switches_count += 1
            if switches_count % 2 != p[bulb]:
                break
        else:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
