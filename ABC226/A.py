"""
https://atcoder.jp/contests/abc226/tasks/abc226_a

入力例
3.456



"""
from decimal import Decimal, ROUND_HALF_UP

print(Decimal(input()).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
