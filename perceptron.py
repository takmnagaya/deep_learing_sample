import numpy as np
import matplotlib.pylab as plt

class Perceptron:
    def __init__(self, w):
        # w is List for weight
        self.w = np.array(w)

    # 活性化関数
    def active_function(self, x):
        tmp_y = sum(self.w * np.array(x))
        return Perceptron.step_function(x)

    # ステップ関数
    def step_function(x):
        y = x > 0
        return y.astype(np.int)

    # ステップ関数描画
    def print_step_function():
        x = np.arange(-1.0, 1.0, 0.1)
        y = Perceptron.step_function(x)
        plt.plot(x, y)
        plt.ylim(-0.1, 1.1) # y軸の表示範囲を指定
        plt.show()

    # 適切にweight, biusを設定すればANDゲートになる
    def AND(x):
        perceptron = Perceptron([0.5, 0.5, -0.7])
        return perceptron.active_function(x)

    # 適切にweight, biusを設定すればNANDゲートになる
    def NAND(x):
        perceptron = Perceptron([-0.5, -0.5, 0.7])
        return perceptron.active_function(x)

    # 適切にweight, biusを設定すればORゲートになる
    def OR(x):
        perceptron = Perceptron([1.0, 1.0, 0.0])
        return perceptron.active_function(x)

    # 一方の入力のみが1の時のみ1を出力する
    def XOR(x):
        l = [Perceptron.OR(x), Perceptron.NAND(x), 1.0]
        return Perceptron.AND(l)

a = [[0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
for x in a:
    print(x[:2])
    print('AND')
    print(Perceptron.AND(x))
    print('NAND')
    print(Perceptron.NAND(x))
    print('OR')
    print(Perceptron.OR(x))
    print('XOR')
    print(Perceptron.XOR(x))

Perceptron.print_step_function()
