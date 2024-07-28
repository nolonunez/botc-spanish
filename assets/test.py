import json

char = "drunk"

with open('./assets/special.json') as fs:
  special_data = json.load(fs)

print(special_data)

for i in special_data:
    if i == char:
        print(special_data[char])

fs.close()