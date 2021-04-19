# import traceback

class Calculator:

    # 相加的功能
    def add(self, a, b):
        return a + b

    # 相减功能
    def sub(self, a, b):
        return a - b

    # 相乘功能
    def mul(self, a, b):
        return a * b

    # 相除功能
    def div(self, a, b):
        while b != 0:
            return a / b
        raise ValueError("被除数不得为0")
