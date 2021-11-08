"""
https://atcoder.jp/contests/abc226/tasks/abc226_e

入力例
3 3
1 2
1 3
2 3

"""


def main():
    n, m = map(int, input().split())
    edges = []
    routes = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        for i, r in enumerate(routes):
            if u in r or v in r:
                routes[i] = routes[i] | {u, v}
                break
        else:
            routes.append({u, v})

    # print(routes)
    route_num = len(routes)
    for i, r1 in enumerate(routes):
        for j, r2 in enumerate(routes):
            if i >= j:
                continue
            if len(r1 & r2):
                print(1, r1, 2, r2)
                route_num -= 1
                break

        else:
            if len(r1) == 2:
                route_num -= 1
    # print(route_num)
    if route_num == 0:
        print(0)
    else:
        print(2 ** route_num)


if __name__ == "__main__":
    main()
