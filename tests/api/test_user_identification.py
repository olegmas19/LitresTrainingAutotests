import json
import allure
from allure_commons.types import Severity
from litres_training_autotests.api.api_requests import api_requests
from jsonschema import validate
from litres_training_autotests.utils.load_schemas import load_schema


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "KING_PLANES")
@allure.feature("Идентификация")
@allure.story("Пользователь может ввести логин в поле 'Почта или логин' и нажать Продолжить")
@allure.suite("API-Тесты")
@allure.title("Идентификация пользователя через API")
def test_user_identification(litres_user):

    # GIVEN
    url = "/auth/login-available"
    payload = json.dumps({"login": litres_user[0]})

    # WHEN
    response = api_requests.api_request(url, method="POST", data=payload)

    # THEN
    assert response.status_code == 200
    assert response.json()["payload"]["data"]["available"] == False
    validate(response.json(), schema=load_schema("/post_user_identification.json"))
