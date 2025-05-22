import allure
from allure_commons.types import Severity
from litres_training_autotests.api.api_requests import api_requests
from jsonschema import validate
from litres_training_autotests.utils.load_schemas import load_schema


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "KING_PLANES")
@allure.feature("Поиск")
@allure.story("Пользователь может найти книгу")
@allure.suite("API-Тесты")
@allure.title("Проверка поиска книги через API")
def test_search_book():

    # GIVEN
    name_book = "Скотный Двор"
    art_types = "text_book"
    types = "text_book"
    url = f"/search?q={name_book}&art_types={art_types}&types={types}"

    # WHEN
    response = api_requests.api_request(url, method="GET")

    # THEN
    assert response.status_code == 200
    assert response.json()["payload"]["data"][0]["instance"]["title"] == name_book
    validate(response.json(), schema=load_schema("/get_search_book.json.json"))
