

class Person:
    name = 'gray'
    age = 16
    gender = 'male'
    __salary = 5000

    # 初始化实例
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = self.__salary

    def eat(self):
        print(f"{self.name} is eating")

    def run(self):
        print(f"{self.name} is running")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def work(self):
        print(f"{self.name} is working")

    def __makeMoney(self):
        print(self.__salary + 10000)

    # 类内调用私有方法
    def _makeMoney(self):
        self.__makeMoney()

    def _selectMoney(self):
        print(self.salary)


class Funny(Person):

    def fun(self):
        print(f"{self.name} is funny")


class Singer(Person):

    # 覆盖父类的_getMoney()
    def _makeMoney(self):
        print(self.salary + 100000)

funny1 = Funny("沈腾", 30, "male")
print(funny1.name)
funny1.fun()

singer1 = Singer("王力宏", 35, "male")
singer1._makeMoney()

p = Person("lilei", 17, "male")
print(p.name)
print(p.salary)
p._makeMoney()
p._selectMoney()