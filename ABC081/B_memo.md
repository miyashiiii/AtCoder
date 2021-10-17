## model answer
https://kihor.com/kp_py_atc_abc081b/
```python
n = input()
a = list(map(int, input().split()))
cnt = 0
while all(i%2==0 for i in a):
  a = [i/2 for i in a]
  cnt += 1
print(cnt)
```

## Point

- L7: all()で一括奇数判定
- L8: 内包表記で一括処理
