import yaml


with open('./data/data.yaml') as f:

    data = yaml.safe_load(f)

print(data)
print(data['default1'])
print(data['default2'])
print(data['default3'])
print(data['default4'])
