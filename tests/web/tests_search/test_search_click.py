import allure
from allure_commons.types import Severity
from litres_training_autotests.pages.web.search_litres import search_litres

@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "KING_PLANES")
@allure.feature("Проверка поиска")
@allure.story("Пользователь может подтвердить результаты ввода кнопкой 'Поиск'")
@allure.description("Простые тесты на проверку поиска")
@allure.suite("UI-Тесты")
@allure.link("https://www.litres.ru/", name="Testing")
@allure.title("Проверка поиска через кнопку 'Поиск'")
def test_search_click():

    # GIVEN
    search_litres.open()

    # WHEN
    search_litres.fill_search("Война и мир")
    search_litres.click_button_search()

    # THEN
    search_litres.checking_search_results(
        "Результаты поиска «Война и мир»", "Война и мир"
    )
