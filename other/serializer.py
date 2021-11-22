import json

data = {
    'name': 'Nick',
    'age': 21
}

# with open('data.json', 'w') as f:
#     json.dump(data, f)

# data2 = json.dumps(data)
# print(data2)
# data = json.loads(data2)
# print(data)
with open('data.json','r') as f:
    data1 = json.load(f)

print(data1)