a = [1, 2, 3, 4, 5, 100, 1000]
print(a)
# >> [1, 2, 3, 4, 5, 100, 1000] # リスト出力

print(len(a))
# >> 7 # リストの長さ出力

print(a[0])
# >> 1 # リストの最初の要素を出力

a[0] = -1
print(a[0])
# >> -1 # 値を代入

print(a[1:2])
# インデックスの1番目から2番目まで出力
# 2番目は含まれない

print(a[1:])
# インデックスの1番目から最後まで出力

print(a[:3])
# インデックスの最初から3番目まで出力
# 3番目は含まれない

print(a[:-1])
# インデックスの最初から最後の一つ前まで出力
