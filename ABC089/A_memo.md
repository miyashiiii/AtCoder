## wrong answer
```python
n = int(input())

for i in range(n):
    t, x, y = [int(c) for c in input().split()]

    if t < x + y or (x + y) % 2 != t % 2:
        print("No")
        exit()

print("Yes")

```

- 上記では1件WAとなる。
- 一つ前の地点からの移動可否も考慮する必要あり。
  - https://qiita.com/Kyan_TK/items/65251777d63e00448a70#%E3%81%AA%E3%81%9C%E5%98%98%E8%A7%A3%E6%B3%95%E3%81%AA%E3%81%AE%E3%81%8B
