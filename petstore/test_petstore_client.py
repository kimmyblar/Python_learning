
import pytest
from faker import Faker
import random
from pet_generator import Pet_Generator
fake = Faker()
#
# @pytest.mark.parametrize("pet_data",
#                          [Pet_Generator.generate_pet()],
#                          ids=["Full params pet"])


def test_add_pet(pet_client):
    pet_data = Pet_Generator.generate_pet()
    response = pet_client.add_pet(pet_data)
    assert response.status_code == 200
    result = pet_client.get_pet(pet_data['id']).json()
    result_dict = {key:value for key, value in result.items() if key in pet_data.keys()}
    assert pet_data == result_dict


def test_delete_pet(pet_client):
    pet_id = 100
    pet_client.add_pet(Pet_Generator.generate_pet())
    assert pet_client.delete_pet(pet_id).status_code == 200
    result = pet_client.get_pet(pet_id)
    assert result.status_code == 404

def test_delete_not_existed_pet(pet_client):
    pet_id = 122
    assert pet_client.delete_pet(pet_id).status_code == 404





