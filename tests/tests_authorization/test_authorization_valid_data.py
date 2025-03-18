import allure
from allure_commons.types import Severity
from Litres_Training_Autotests.authorisation_litres import AuthorisationLitres

@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "KING_PLANES")
@allure.feature("Авторизация пользователя")
@allure.story("Пользователь может авторизоваться с валидными данными")
@allure.description("Простые тесты на проверку авторизации пользователя")
@allure.suite("UI-Тесты")
@allure.link("https://www.litres.ru/", name="Testing")
@allure.title("Авторизация с валидными данными")
def test_checking_authorisation_valid_data():
    authorisation_litres = AuthorisationLitres()

    #GIVEN
    authorisation_litres.open()

    #WHEN
    authorisation_litres.press_tab_login()
    authorisation_litres.fill_login('tracktor19@mail.ru')
    authorisation_litres.press_continue()
    authorisation_litres.fill_password('Ttrraacc')
    authorisation_litres.press_enter()
    authorisation_litres.personal_account_entrance()

    #THEN
    authorisation_litres.should_have_authorized('tracktor19@mail.ru', 'Выход')




