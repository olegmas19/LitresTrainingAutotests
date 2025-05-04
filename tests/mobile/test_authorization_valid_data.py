import allure
from allure_commons._allure import step
from allure_commons.types import Severity
from litres_training_autotests.helper.load_login_pass import load_env
from litres_training_autotests.page.mobile.authorization_mobile import auth_mobile
from litres_training_autotests.page.mobile.skip_onboarding import skip_mobile_onboarding


@allure.tag("mobile")
@allure.severity(Severity.MINOR)
@allure.label("owner", "KING_PLANES")
@allure.feature("Проверка авторизации")
@allure.story(
    "Пользователь может авторизоваться в мобильном приложении с валидными данными"
)
@allure.description("Простые тесты на проверку авторизации")
@allure.suite("mobile-Тесты")
@allure.title("Проверка авторизации с валидными данными")
def test_search():
    litres_login, litres_password = load_env()

    with step("Type search"):
        # GIVEN
        skip_mobile_onboarding.skip_onboarding()

        # WHEN
        auth_mobile.authorisation_mobile(litres_login, litres_password)

        # THEN
        auth_mobile.check_authorisation_valid_result(litres_login)
