import yaml
from Animal import Cat, Dog,main_cat,main_dog


if __name__ == '__main__':

    with open('./data.yaml') as f:
        data = yaml.load(f)

    mimi = Cat(data['mimi'])
    main_cat(mimi)
    wangcai = Dog(data['wangcai'])
    main_cat(wangcai)




