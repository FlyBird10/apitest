from unittest.mock import MagicMock


class Simple():
    def add(self, a, b):
        return a+b

    def plus(self, a, b):
        return a*b


class Calcu():
    def __init__(self):
        self.s = Simple()

    def complex(self, a, b):
        x = self.s.add(a, b)
        y = self.s.plus(a, b)
        return x+y


if __name__ == '__main__':
    c = Calcu()
    Calcu.plus = MagicMock(return_value=2)  # 当调用add方法时返回 2
    # print(c.add(1, 7))
    print(c.complex(3, 2))