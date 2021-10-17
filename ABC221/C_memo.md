## model answer
https://atcoder.jp/contests/abc221/editorial/2730
```python
N=sorted(input())[::-1]
A=N[0::2]
B=N[1::2]

for i in range(min(len(A),len(B))):
  if A[i]!=B[i]:
    A[i],B[i]=B[i],A[i]
    break
      
print(int("".join(A))*int("".join(B)))

```

## Point
- 闇雲に操作せず、目的を条件を満たす条件を考える
  - とはいえ上記のアルゴリズムは自分では思いつかない
- L5: 奇数文字目はN[0::2],偶数文字目はN[1::2]で取得できる
  - 2次元配列をsort()すると先頭の値でソートされる
    - 引数keyを指定することで任意の要素でソートできる
- L20: 勝数をマイナスで表現
  - 昇順ソートでrankを求められる
- L7 関数名はシンプルに、必要ならコメントで補足
  - 関数名にこだわって下手に長ったらしくなるのも読みにくい
  - 名付けに悩むのも時間の無駄