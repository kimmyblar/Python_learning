from tkinter.font import names

from faker import Faker
import random


fake = Faker()

class Pet_Generator:
    @staticmethod
    def generate_pet(**kwargs):
        pet_data = {
            'id':Pet_Generator.generate_id(),
            'category':Pet_Generator.generate_category(),
            'photoUrls':Pet_Generator.generate_url(),
            'tags':Pet_Generator.generate_tags(),
            'status':Pet_Generator.generate_status()



        }
        for k in kwargs.keys():
            if k not in pet_data:
                raise KeyError(f'Ключ {k} не содержится в словаре')

        # pet_data['id'] = kwargs['id']
        print(kwargs)
        pet_data.update(kwargs)
        return pet_data
    @staticmethod
    def generate_id():
        return random.randint(10,100)
    @staticmethod
    def generate_category():
        return {'id':Pet_Generator.generate_id(),
                'name': random.choice(['Cats', 'Dogs', 'Fish'])}
    @staticmethod
    def generate_url():
        return [fake.image_url() for i in range(random.randint(0,10))]
    @staticmethod
    def generate_tags():
        return [{'id':Pet_Generator.generate_id(),
                'name':random.choice(['New', 'Young', 'Old'])}],
    @staticmethod
    def generate_status():
        return random.choice(['available', 'unavailable'])




# pet_1 = Pet_Generator()
# new_pet = pet_1.generate_pet()
# print(new_pet)

# new_pet = Pet_Generator.generate_pet(id=100, status='available', name='Bob')
# print(new_pet)