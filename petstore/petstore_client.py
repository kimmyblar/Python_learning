
import requests
petstore_url = 'https://petstore.swagger.io/v2/'
json_data_post = {"name": "Dranik", "photoUrls": ["string"]}
json_data_put = {"name": "Dranik", "photoUrls": ["string"],"status": "available" }
pet_url = 'pet/'
store_url = 'store/'
user_url = 'user/'
id = '9223372036854775807'


response = requests.request('POST', f'{petstore_url}{pet_url}', json=json_data_post)
print(response.json())

response = requests.request('PUT', f'{petstore_url}{pet_url}', json=json_data_put)
print(response.json())

response = requests.request('GET', f'{petstore_url}{pet_url}{id}')
print(response.json())

response = requests.request('DELETE', f'{petstore_url}{pet_url}{id}')
print(response.json())

# Думала сделать бесконечный цикл, даже понимаю как это делать на уровне логики
# (Надо как-то вытащить из json post id и после создания сущности подставлять ее id в нашу переменную id
# После чего у нас всегда будет работать создание, изменение, получение и удаление сущности
# Возможно это тема следующего урока, пока оставила так
