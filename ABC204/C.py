"""
https://atcoder.jp/contests/abc204/tasks/abc204_c

3 3
1 2
2 3
3 2
"""

from sys import setrecursionlimit

setrecursionlimit(40000)


def main():
    def dfs(node):
        # 探索済みならreturn
        if visited[node] == 1:
            return

        # 探索済みフラグを立てる
        visited[node] = 1

        # 各edgeに対して更に探索
        for e in edges[node]:
            if visited[e] == 1:
                continue
            dfs(e)

    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)

    ans = 0
    for i in range(n):
        # 未探索なら0, 探索済みは1
        visited = [0] * n
        dfs(i)
        ans += sum(visited)

    print(ans)


if __name__ == "__main__":
    main()
