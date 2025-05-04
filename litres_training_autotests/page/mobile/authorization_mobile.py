from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have
import allure


class AuthorizationMobile:

    @allure.step("Авторизация в мобильном приложении")
    def authorisation_mobile(self, litres_login, litres_password):
        browser.element(
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().resourceId("ru.litres.android:id/navigation_bar_item_icon_view").instance(4)',
            )
        ).should(be.visible).click()
        browser.element((AppiumBy.ID, "ru.litres.android:id/login_button")).should(
            be.visible
        ).click()
        browser.element((AppiumBy.ID, "ru.litres.android:id/login")).should(
            be.visible
        ).click().type(litres_login)
        browser.element((AppiumBy.ID, "ru.litres.android:id/password")).should(
            be.visible
        ).click().type(litres_password)
        browser.element((AppiumBy.ID, "ru.litres.android:id/sign_in_btn")).should(
            be.visible
        ).click()

    @allure.step("Проверка результатов успешной авторизации")
    def check_authorisation_valid_result(self, litres_login):
        browser.element((AppiumBy.ID, "ru.litres.android:id/user_login")).should(
            be.visible
        ).should(have.text(litres_login))

    @allure.step("Проверка результатов неуспешной авторизации")
    def check_authorisation_invalid_result(self):
        browser.element((AppiumBy.ID, "ru.litres.android:id/error_text_message")).should(
            be.visible
        ).should(have.text("Invalid username or password. Please make sure you have entered your information correctly."))


auth_mobile = AuthorizationMobile()
