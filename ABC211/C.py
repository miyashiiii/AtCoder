"""
https://atcoder.jp/contests/abc211/tasks/abc211_c

chchokudai
"""


def main():
    s = input()

    chokudai = "chokudai"
    # i文字目までの組み合わせの数の配列
    counts = [0] * len(chokudai)
    for c in s:
        if c not in chokudai:
            continue

        # chokudaiに含まれる文字の場合
        idx = chokudai.index(c)
        if idx == 0:
            counts[0] += 1
            continue

        # 作れる組み合わせの数は、idx-1の組み合わせの数分増える
        counts[idx] += counts[idx - 1]

    ans = counts[-1] % (10 ** 9 + 7)
    print(ans)


if __name__ == "__main__":
    main()
