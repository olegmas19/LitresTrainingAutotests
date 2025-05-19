import allure
from allure_commons.types import Severity
from litres_training_autotests.pages.web.authorization_litres import authorization_litres


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "KING_PLANES")
@allure.feature("Авторизация пользователя")
@allure.story("Пользователь не может авторизоваться с невалидными данными")
@allure.description("Простые тесты на проверку авторизации пользователя")
@allure.suite("UI-Тесты")
@allure.link("https://www.litres.ru/", name="Testing")
@allure.title("Невозможность авторизации с невалидными данными")
def test_checking_authorization_invalid_data():

    # GIVEN
    authorization_litres.open()

    # WHEN
    authorization_litres.press_tab_login()
    authorization_litres.fill_login("qweasdzxc")
    authorization_litres.press_continue()
    authorization_litres.fill_password("qweasdzxc")
    authorization_litres.press_enter()

    # THEN
    authorization_litres.should_not_have_authorized(
        "Ввести пароль", "Неверное сочетание логина и пароля", "Войти"
    )
