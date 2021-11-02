"""
https://atcoder.jp/contests/abc128/tasks/abc128_c

5 3
1 2
2 3
1 3

"""


def main():
    n, m = map(int, input().split())

    friends = []
    for i in range(m):
        friend = {int(i) - 1 for i in input().split()}
        friends.append(friend)
    # print(friends)

    ans = 0

    for i in range(2 ** n):
        # print(bin(i))
        members = []
        for j in range(n):
            # 順に右にシフトさせ最下位bitのチェックを行う
            if (i >> j) & 1:
                members.append(j)
        can_group = True
        for m1 in members:
            for m2 in members:
                if m1>=m2:
                    continue
                if {m1, m2} not in friends:
                    can_group = False
                    break
        if can_group:
            ans = max(ans, len(members))

    print(ans)


if __name__ == "__main__":
    main()
