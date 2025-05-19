import allure
from allure_commons.types import Severity
from litres_training_autotests.helper.api_requests import api_requests


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "KING_PLANES")
@allure.feature("Избранное")
@allure.story("Пользователь может добавить товар в избранное")
@allure.suite("API-Тесты")
@allure.title("Проверка добавления товара в избранное через API")
def test_add_book_to_favorites():

    # GIVEN
    url = "/wishlist/arts/8685806"

    # WHEN
    response = api_requests.api_request(url, method="PUT")

    # THEN
    assert response.status_code == 204
    assert response.text == ""
