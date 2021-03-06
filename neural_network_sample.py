# 3階層ニューラルネットワークの実装
# 入力(x1, x2) -> 出力(y1, y2)
# 中間層1 z11, z12, z13
# 中間層2 z21, z22
import numpy as np

class NeuralNetworkSample:
    def __init__(self, x1, x2):
        self.x = np.array([x1, x2])
        self.w1 = np.array([[1.0, 1.0], [-0.8, 0.5], [0.2, -1.0]])
        self.b1 = np.array([-0.5, 0.1, 0.8])
        self.w2 = np.array([[1.0, 2.0, -3.0], [-1.0, 1.0, 2.0]])
        self.b2 = np.array([0.1, 0.8])
        self.w3 = np.array([[1.0, -3.0], [-1.0, 2.0]])
        self.b3 = np.array([0.1, 0.8])

    # sigmoid関数
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    # 恒等関数
    def identity_function(x):
        return x

    # ソフトマックス関数
    def softmax(x):
        m = np.max(x)
        return np.exp(x - m) / np.sum(np.exp(x - m))

    def forward(self):
        self.z1 = NeuralNetworkSample.sigmoid(np.dot(self.w1, self.x) + self.b1)
        self.z2 = NeuralNetworkSample.sigmoid(np.dot(self.w2, self.z1) + self.b2)
        self.y = NeuralNetworkSample.identity_function(np.dot(self.w3, self.z2) + self.b3)
        return self.y

n = NeuralNetworkSample(1.0, 2.0)
print(n.forward())
print('softmax')
a = np.arange(0, 1, 0.01)
print(NeuralNetworkSample.softmax(a))
