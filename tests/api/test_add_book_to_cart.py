import json
import allure
from allure_commons.types import Severity
from litres_training_autotests.helper.api_requests import api_requests
from jsonschema import validate
from litres_training_autotests.helper.load_schemas import load_schema


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "KING_PLANES")
@allure.feature("Корзина")
@allure.story("Пользователь может добавить товар в корзину")
@allure.suite("API-Тесты")
@allure.title("Проверка добавления товара в корзину через API")
def test_add_book_to_cart():

    # GIVEN
    url = "/cart/arts/add"
    art_ids = [71923111]
    headers = {
        "Content-Type": "application/json",
    }
    payload = json.dumps({"art_ids": art_ids})

    # WHEN
    response = api_requests.api_request(
        url, method="PUT", data=payload, headers=headers
    )

    # THEN
    assert response.status_code == 200
    assert response.json()["payload"]["data"]["added_art_ids"] == art_ids
    validate(response.json(), schema=load_schema("/put_add_book_to_cart.json"))
