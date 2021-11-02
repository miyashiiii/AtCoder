"""
https://atcoder.jp/contests/abc077/tasks/arc084_a

2
1 5
2 4
3 6

"""
import bisect


def main():
    n = int(input())

    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    c_list = list(map(int, input().split()))
    a_list.sort()
    b_list.sort()
    c_list.sort()
    ans = 0

    for b in b_list:
        # print("b:", b)
        a_num = bisect.bisect_left(a_list, b)
        c_num = len(c_list) - bisect.bisect_right(c_list, b)
        # print("a_num:", a_num)
        # print("c_num:", c_num)
        ans += a_num * c_num

    print(ans)


if __name__ == "__main__":
    main()
