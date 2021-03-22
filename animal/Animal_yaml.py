import yaml
from Animal import Cat, Dog,main_cat,main_dog


if __name__ == '__main__':

    with open(r'./data.yaml') as f:
        data = yaml.safe_load(f)
        mimi = Cat(**data['cat'])
        main_cat(mimi)
        wangcai = Dog(**data['dog'])
        main_dog(wangcai)




