import json

people_string = '''{ 
    "people":[ 
        { 
        "name": "Kishan Billava",
        "phone": 123456789,
        "emails":["kishanbillava@homemail.com","kishanbillava@workmail.com"],
        "has_license": false
        },
        {
        "name": "Rock Star",
        "phone": 987654321,
        "emails":null,
        "has_license": true
        }

         ] 
    }
    '''


data = json.loads(people_string)
print(data)
print(type(data['people']))
# print(data['people'][1]['name'])

for person in data['people']:
    print(person['name'])

for person in data['people']:
    del person['phone']


new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)