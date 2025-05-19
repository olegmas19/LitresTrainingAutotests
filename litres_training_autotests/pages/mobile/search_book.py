from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be
import allure


class SearchBook:

    @allure.step("Поиск книги через строку поиска по названию")
    def search_book(self, name_book, name_book_full):
        browser.element((AppiumBy.ID, "ru.litres.android:id/search")).should(
            be.visible
        ).click()
        browser.element((AppiumBy.ID, "ru.litres.android:id/et_search_query")).should(
            be.visible
        ).type(f"{name_book}")
        browser.element(
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{name_book_full}")')
        ).should(be.visible).click()


    @allure.step("Проверка результатов поиска")
    def check_search_result(self, value1):
        browser.element(
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{value1}")')
        ).should(be.visible)


search_litres = SearchBook()
