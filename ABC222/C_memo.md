## model answer
```python
N,M = map(int,input().split())
S = [input() for i in range(2*N)]
rank = [[0,i] for i in range(2*N)]
# rank[i] = [x,y]  -> i位なのは -x勝で人y

def judge(a,b):
  # 引き分けなら-1,前者勝ちなら0,後者勝ちなら1
  if a==b: return -1
  if a=='G' and b=='P': return 1
  if a=='C' and b=='G': return 1
  if a=='P' and b=='C': return 1
  return 0

for j in range(M):
  for i in range(N):
    player1 = rank[2*i][1]
    player2 = rank[2*i+1][1]
    result = judge(S[player1][j], S[player2][j])
    if result !=-1: rank[2*i+result][0] -= 1
  rank.sort()
for _,i in rank: print(i+1)

```

## Point

- L4: ランクを2次元配列に
  - 2次元配列をsort()すると先頭の値でソートされる
    - 引数keyを指定することで任意の要素でソートできる
- L20: 勝数をマイナスで表現
  - 昇順ソートでrankを求められる
- L7 関数名はシンプルに、必要ならコメントで補足
  - 関数名にこだわって下手に長ったらしくなるのも読みにくい
  - 名付けに悩むのも時間の無駄