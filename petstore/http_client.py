import requests
from requests.exceptions import JSONDecodeError

class HttpClient:
    def  __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def _request(self, method, endpoint, **kwargs):
        print(f'Выполнен запрос для метода {method} и {endpoint}:'
              f'Содержимое запроса:  {kwargs}')
        request_answer = self.session.request(method, endpoint, **kwargs)
        if request_answer.status_code == 200:
            print (f'Код ответа на ваш запрос: {request_answer.status_code}'
                   f'Ответ на ваш запрос: {request_answer.json()}')
        else:
            try:
                answer = request_answer.json()
            except JSONDecodeError:
                answer = request_answer.text
            print(f'Код ответа на ваш запрос: {request_answer.status_code}'
                  f'Ответ на ваш запрос: {answer}')

        return request_answer

    def get(self, endpoint, params=None):
        return self._request('GET', f'{self.url}{endpoint}', params=params)

    def post(self, endpoint, json):
        return self._request('POST', f'{self.url}{endpoint}', json=json)

    def put(self, endpoint, json):
        return self._request('PUT', f'{self.url}{endpoint}', json=json)

    def delete(self, endpoint):
        return self._request('DELETE', f'{self.url}{endpoint}')




# client = HttpClient('https://petstore.swagger.io/v2/')
# response = client.get('pet/9223372036854775807')
# print(response.json())
# response = client.post('pet', {"name": "Dranik", "photoUrls": ["string"]})
# print(response.json())

