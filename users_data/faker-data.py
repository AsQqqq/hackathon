from mimesis import Person
import uuid
import json

prs = Person('ru')

data = []
for _ in range(0, 1000):
    phone_number = prs.phone_number()
    email = prs.email()
    id = uuid.uuid4()
    data.append({
        'phone_number': phone_number,
        'email': email,
        'id': str(id)
    })
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

