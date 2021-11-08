"""
https://atcoder.jp/contests/abc226/tasks/abc226_e

入力例
3 3
1 2
1 3
2 3

"""


def main():
    n = int(input())
    seq = []
    for i in range(n + 1):
        if i <= 1:
            seq.append(1)
            continue
        seq.append(seq[i - 1] + seq[i - 2])

    print(seq[-1])


if __name__ == "__main__":
    main()
