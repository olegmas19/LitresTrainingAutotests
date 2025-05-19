import allure
from allure_commons.types import Severity
from litres_training_autotests.pages.web.authorization_litres import authorization_litres


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "KING_PLANES")
@allure.feature("Авторизация пользователя")
@allure.story("Пользователь не может авторизоваться с пустым полем 'почта или логин'")
@allure.description("Простые тесты на проверку авторизации пользователя")
@allure.suite("UI-Тесты")
@allure.link("https://www.litres.ru/", name="Testing")
@allure.title("Невозможность авторизации с пустым полем 'почта или логин'")
def test_authorization_empty_field_login_email():

    # GIVEN
    authorization_litres.open()

    # WHEN
    authorization_litres.press_tab_login()
    authorization_litres.fill_login("")
    authorization_litres.press_continue()

    # THEN
    authorization_litres.login_cannot_be_empty(
        "Поле не может быть пустым", "Продолжить"
    )
