class Man:
    def __init__(self, name):
        # コンストラクタ
        self.name = name
        # インスタンス変数の作成

    def hello(self):
        # インスタンス変数へのアクセス
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Goodbye " + self.name + "!")

m = Man('takmnagaya')
m.hello()
m.goodbye()
