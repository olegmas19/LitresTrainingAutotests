import allure
from allure_commons._allure import step
from allure_commons.types import Severity
from litres_training_autotests.page.mobile.search_book import search_litres
from litres_training_autotests.page.mobile.skip_onboarding import skip_mobile_onboarding


@allure.tag("mobile")
@allure.severity(Severity.MINOR)
@allure.label("owner", "KING_PLANES")
@allure.feature("Проверка поиска")
@allure.story("Пользователь может найти книгу через строку поиска в приложении")
@allure.description("Простые тесты на проверку поиска")
@allure.suite("mobile-Тесты")
@allure.title("Проверка поиска через строку поиска")
def test_search():
    with step("Type search"):
        name_book = "скотный двор"
        name_book_full = "джордж оруэлл скотный двор"
        name_book_result = "Скотный двор / Animal Farm"

        # GIVEN
        skip_mobile_onboarding.skip_onboarding()

        # WHEN
        search_litres.search_book(name_book, name_book_full)

        # THEN
        search_litres.check_search_result(name_book_result)
