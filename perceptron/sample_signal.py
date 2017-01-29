import numpy as np
class Perceptron:
    def __init__(self, w):
        # w is List for weight
        self.w = np.array(w)

    # 活性化関数
    def active_function(self, x):
        tmp_y = sum(self.w * np.array(x))
        if tmp_y > 0:
            return 1
        else:
            return 0

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

a = [[0.0, 0.0, 1.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
for x in a:
    print(x[:2])
    print('AND')
    print(Perceptron.AND(x))
    print('NAND')
    print(Perceptron.NAND(x))
    print('OR')
    print(Perceptron.OR(x))
