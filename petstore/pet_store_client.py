from http_client import HttpClient

class PetClient(HttpClient):
    def __init__(self):
        url = 'https://petstore.swagger.io/v2'
        super().__init__(url)


    def add_pet(self, pet_data):
        return self.post('/pet', json=pet_data)

    def get_pet(self, pet_id):
        return self.get(f'/pet/{pet_id}')

    def put_pet(self, pet_data):
        return self.put('/pet/', json=pet_data)

    def delete_pet(self, pet_id):
        return self.delete(f'/pet/{pet_id}')

