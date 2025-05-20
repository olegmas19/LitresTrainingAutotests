import allure
from allure_commons.types import Severity
from litres_training_autotests.pages.web.authorization_litres import authorization_litres

@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "KING_PLANES")
@allure.feature("Авторизация пользователя")
@allure.story("Пользователь может авторизоваться с валидными данными")
@allure.description("Простые тесты на проверку авторизации пользователя")
@allure.suite("UI-Тесты")
@allure.link("https://www.litres.ru/", name="Testing")
@allure.title("Авторизация с валидными данными")
def test_checking_authorization_valid_data(load_env):

    # GIVEN
    authorization_litres.open()

    # WHEN
    authorization_litres.press_tab_login()
    authorization_litres.fill_login(load_env[0])
    authorization_litres.press_continue()
    authorization_litres.fill_password(load_env[1])
    authorization_litres.press_enter()
    authorization_litres.personal_account_entrance()

    # THEN
    authorization_litres.should_have_authorized(load_env[0], "Выход")
