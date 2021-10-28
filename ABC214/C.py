"""
https://atcoder.jp/contests/abc214/tasks/abc214_c

3
4 1 5
3 10 100
"""


def main():
    n = int(input())
    s_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))

    ans = t_list

    # 2周分回す
    for i in range(n * 2):
        idx = i % n
        next_idx = (i + 1) % n
        tmp_next_ans = ans[idx] + s_list[idx]
        if tmp_next_ans < ans[next_idx]:
            ans[next_idx] = tmp_next_ans

    for v in ans:
        print(v)


if __name__ == "__main__":
    main()
