import allure
import pytest
from utils.api_client import ApiClient

BASE_URL = "https://petstore3.swagger.io/api/v3"
pet_id = 99
pet_name = "Rocky"
pet_name_new = "Timber"

@pytest.fixture
def api_client():
    return ApiClient(BASE_URL)

@allure.feature("[api test] Создание питомца")
@allure.story("Позитивный тест")
def test_create_pet(api_client):
    with allure.step("Тело запроса на создание питомца"):
        data = {
            "id": pet_id,
            "name": pet_name,
            "category": {"id": 1, "name": "dogs"},
            "photoUrls": ["https://example.com/photo.jpg"],
            "status": "available"
        }

    with allure.step("Отправить POST запрос"):
        response = api_client.post("/pet", data=data)

    with allure.step("Проверка ответа"):
        assert response.status_code == 200
        assert response.json()["name"] == pet_name

@allure.feature("[api test] Получение питомца по его ID")
@allure.story("Позитивный тест")
def test_get_pet(api_client):

    with allure.step("Отправить GET запрос"):
        response = api_client.get(f"/pet/{pet_id}" )

    with allure.step("Проверка ответа"):
        assert response.status_code == 200
        assert response.json()["id"] == pet_id

@allure.feature("[api test] Обновление данных питомца")
@allure.story("Позитивный тест")
def test_update_pet(api_client):
    with allure.step("Измененные данные питомца"):
        data = {
            "id": pet_id,
            "name": pet_name_new,
            "category": {"id": 1, "name": "dogs"},
            "photoUrls": ["https://example.com/photo.jpg"],
            "tags": [{"id": 1, "name": "tag1"}],
            "status": "available"
        }

    with allure.step("Отправить PUT запрос"):
        response = api_client.put("/pet", data=data)

    with allure.step("Проверка ответа"):
        assert response.status_code == 200
        assert response.json()["name"] == pet_name_new

@allure.feature("[api test] Удаление питомца")
@allure.story("Позитивный тест")
def test_delete_pet(api_client):
    with allure.step("Отправить DELETE запрос"):
        response = api_client.delete(f"/pet/{pet_id}")

    with allure.step("Проверка ответа"):
        assert response.status_code == 200

@allure.feature("[api test] Получение питомца по его ID")
@allure.story("Негативный тест")
def test_get_pet_negative(api_client):
    with allure.step("Отправить GET запрос"):
        response = api_client.get(f"/pet/666666")

    with allure.step("Проверка ответа"):
        assert response.status_code == 404