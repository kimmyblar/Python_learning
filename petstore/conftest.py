import pytest
from http_client import HttpClient
from pet_store_client import PetClient

@pytest.fixture(scope='module')
def client():
    return HttpClient('https://petstore.swagger.io/v2/')

@pytest.fixture(scope='module')
def pet_client():
    return PetClient()

