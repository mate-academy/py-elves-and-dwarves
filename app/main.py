def calc(a, b):
    def add():
        return a + b

    def sub():
        return a - b

    calc.add = add
    calc.sub = sub

    return calc


user_calc = calc(2, 4)
print(user_calc.add())
print(user_calc.sub())
print(dir(calc))