# NumPyは外部ライブラリなので、Pythonの標準ライブラリに含まれておらず、
# 明示的に読み込む必要がある
# NumPyに関するメソッドはnpとして参照可能
import numpy as np

# NumPy配列の生成
x = np.array([1.0, 2.0, 3.0, 4.0])
print(x)
print(type(x))
# >> <class 'numpy.ndarray'>

# NumPyの算術計算
x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([2.0, 3.0, 4.0, 5.0])

# 注意!! xとyの配列の要素数が異なるとエラーになる
# 加算
print(x + y)
# 減算
print(x - y)
# 乗算
print(x * y)
# 除算
print(x / y)

# NumPy配列と単一の数値(スカラ値)との組み合わせの算術計算は可能
x = np.array([1.0, 2.0, 3.0, 4.0])
y = 2.0
# 加算
print(x + y)
# 減算
print(x - y)
# 乗算
print(x * y)
# 除算
print(x / y)

