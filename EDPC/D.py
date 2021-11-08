"""
https://atcoder.jp/contests/dp/tasks/dp_d

3 8
3 30
4 50
5 60




"""


def main():
    n, max_w = map(int, input().split())
    dp_table = [[0 for _ in range(n)] for _ in range(max_w)]
    for i in range(n):
        w, v = map(int, input().split())
        w -= 1
        for j in range(max_w):
            if j < w:
                if i == 0:
                    continue
                dp_table[j][i] = dp_table[j][i - 1]
                continue
            if j == w:
                dp_table[j][i] = v
                continue
            dp_table[j][i] = max(dp_table[j][i - 1], dp_table[j - w - 1][i - 1] + v)
        # print(dp_table)

    # 商品n個のときの最大値
    print(max([row[-1] for row in dp_table]))


if __name__ == "__main__":
    main()
