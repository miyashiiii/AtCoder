"""
https://atcoder.jp/contests/abc079/tasks/abc079_c

1222
"""


def main():
    a, b, c, d = list(map(int, input()))
    for i in range(2 ** 3):
        ops = []
        ans = a

        for j in range(3):
            # 順に右にシフトさせ最下位bitのチェックを行う
            if (i >> j) & 1:
                ans += [b, c, d][j]
                ops.append("+")

            else:
                ans -= [b, c, d][j]
                ops.append("-")
        if ans == 7:
            print(f"{a}{ops[0]}{b}{ops[1]}{c}{ops[2]}{d}=7")
            return


if __name__ == "__main__":
    main()
