
class Animal:

    name:str
    age:int
    gender:str
    color:str

    def __init__(self, name, age, gender,color):
        self.name = name
        self.age = age
        self.gender = gender
        self.color = color

    def call(self):
        print(f"{self.name}会叫")

    def run(self):
        print(f"{self.name}会跑")


class Cat(Animal):

    hair = 'shorthair'

    def __init__(self, name, age, gender, color, hair = 'shorthair'):
        super().__init__(name, age, gender,color)
        self.hair = hair

    def catch(self):
        print(f"{self.name} 会捉老鼠")

    def call(self):
        print(f"{self.name}会喵喵叫")



class Dog(Animal):

    hair = 'longhair'
    
    def __init__(self, name, age, gender, color, hair = 'longhair'):
        super().__init__(name, age, gender,color)
        self.hair = hair

    def watch(self):
        print(f"{self.name}会看家")

    def call(self):
        print(f"{self.name}会汪汪叫")


def main_cat(f):
    f.catch()
    print(f"{f.name} {f.color} {f.age} {f.gender} {f.hair} 捉到了老鼠")

def main_dog(f):
    f.watch()
    print(f"{f.name} {f.color} {f.age} {f.gender} {f.hair}")


if __name__ == '__main__':
    cat = Cat('mimi',2,'male','black')
    main_cat(cat)

    dog = Dog('wangcai',3,'female','white')
    main_dog(dog)