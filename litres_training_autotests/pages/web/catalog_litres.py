from selene import browser, be, by
import allure
from selene.support.shared.jquery_style import s


class CatalogLitres:

    @allure.step("Открытие сайта 'Литрес'")
    def open(self):
        browser.open("/")

    @allure.step("Переход в каталог")
    def go_to_catalog(self):
        browser.element('[data-testid="header-catalog-button"]').click()

    @allure.step("Проверка наличия категорий в каталоге")
    def check_texts_on_page(self, *texts):
        for text in texts:
            s(by.text(text)).should(be.visible)


catalog_litres = CatalogLitres()
