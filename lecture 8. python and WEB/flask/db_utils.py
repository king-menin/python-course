import json

user_credentials = {}
user_email = {}
user_data = {}

def load_database():
    with open('user_credentials.json', 'r') as fin:
        user_credentials.clear()
        user_credentials.update(json.load(fin))
    with open('user_email.json', 'r') as fin:
        user_email.clear()
        user_email.update(json.load(fin))
    with open('user_data.json', 'r') as fin:
        user_data.clear()
        user_data.update(json.load(fin))

def store_database():
    with open('user_credentials.json', 'w') as fout:
        json.dump(user_credentials, fout)
    with open('user_email.json', 'w') as fout:
        json.dump(user_email, fout)
    with open('user_data.json', 'w') as fout:
        json.dump(user_data, fout)

