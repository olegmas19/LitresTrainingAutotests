import allure
from allure_commons.types import Severity
from litres_training_autotests.api.api_requests import api_requests


@allure.tag("API")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "KING_PLANES")
@allure.feature("Избранное")
@allure.story("Пользователь может удалить товар из избранного")
@allure.suite("API-Тесты")
@allure.title("Проверка удаления товара из избранного через API")
def test_remove_book_from_favorites():

    # GIVEN
    url = "/wishlist/arts/8685806"

    # WHEN
    response = api_requests.api_request(url, method="DELETE")

    # THEN
    assert response.status_code == 204
    assert response.text == ""
