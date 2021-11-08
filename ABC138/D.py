"""
https://atcoder.jp/contests/abc128/tasks/abc128_c

4 3
1 2
2 3
2 4
2 10
1 100
3 1


"""
import sys

sys.setrecursionlimit(10**7)


def input():
    return sys.stdin.readline()[:-1]


def main():
    n, q = map(int, input().split())
    nodes = [[0, []] for _ in range(n)]  # ans, edges
    for i in range(n - 1):
        a, b = map(int, input().split())
        nodes[a - 1][1].append(b - 1)
        nodes[b - 1][1].append(a - 1)

    for i in range(q):
        p, x = map(int, input().split())
        nodes[p - 1][0] += x

    def dfs(id_, parent):
        for c in nodes[id_][1]:
            if c == parent:
                continue
            nodes[c][0] += nodes[id_][0]
            dfs(c, id_)

    dfs(0, -1)
    print(*[str(n[0]) for n in nodes])


if __name__ == "__main__":
    main()
