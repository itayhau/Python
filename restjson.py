import requests
import json

req = requests.get('https://jsonplaceholder.typicode.com/users')
print("HTTP Status Code: " + str(req.status_code))
print(req.headers)
json_response = json.loads(req.content)
print( json_response[0])
dic = json_response[0]
print(dic.values())

class _User:
   def __init__(self, id, name, username, email, **kwargs):
       self.id = id
       self.name = name
       self.username = username
       self.email = email
   def __str__(self):
       return f'id: {self.id}, name : {self.name}, username : {self.username}, email : {self.email}'

u = _User(**dic)
print()
print(u)

# Quicker
class User:
   def __init__(self):
       pass
   def __str__(self):
       res = " ";
       for k, v in self.__dict__.items():
           res += f"{k} : {v} "
       return res

u = User()
u.__dict__ = dic
print()
print(u.name)
print(u)
