import allure
from allure_commons.types import Severity
from litres_training_autotests.pages.mobile.authorization_mobile import auth_mobile
from litres_training_autotests.pages.mobile.skip_onboarding import skip_mobile_onboarding


@allure.tag("mobile")
@allure.severity(Severity.MINOR)
@allure.label("owner", "KING_PLANES")
@allure.feature("Проверка авторизации")
@allure.story(
    "Пользователь не может авторизоваться в мобильном приложении с невалидными данными"
)
@allure.description("Простые тесты на проверку авторизации")
@allure.suite("mobile-Тесты")
@allure.title("Проверка авторизации с невалидными данными")
def test_authorization_mobile_invalid_data(litres_user):

    # GIVEN
    skip_mobile_onboarding.skip_onboarding()

    # WHEN
    auth_mobile.authorization_mobile(litres_user[0], 'qwerty')

    # THEN
    auth_mobile.check_authorization_invalid_result()
