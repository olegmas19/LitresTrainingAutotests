from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be
import allure


class SkipOnboarding:

    @allure.step("Пропускаем онбординг")
    def skip_onboarding(self):
        browser.element(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ENGLISH")')
        ).click()
        browser.element((AppiumBy.ID, "ru.litres.android:id/choosebutton")).click()
        notification = browser.element(
            (AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button")
        ).wait_until(be.visible)
        if notification:
            browser.element(
                (
                    AppiumBy.ID,
                    "com.android.permissioncontroller:id/permission_deny_button",
                )
            ).click()
        browser.element(
            (AppiumBy.ID, "ru.litres.android:id/btnEnableAdultContent")
        ).should(be.visible).click()


skip_mobile_onboarding = SkipOnboarding()
