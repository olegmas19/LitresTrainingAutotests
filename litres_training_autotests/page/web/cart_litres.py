from selene import browser, have, by, be
import allure
from selene.support.shared.jquery_style import s


class CartLitres:

    @allure.step("Открываем страницу с книгой")
    def open(self, endpoint):
        browser.open(f"{endpoint}")

    @allure.step("Добавляем товар в корзину")
    def add_book_to_card(self):
        browser.element('[data-testid="icon_cart"]').click()

    @allure.step("Закрываем появившееся окно с акцией")
    def close_modal_window(self):
        browser.element('[data-testid="modal__close--button"]').click()

    @allure.step("Переходим в корзину")
    def go_to_cart(self):
        browser.element('[data-testid="header__cart--counter"]').click()

    @allure.step("Проверяются наличие товара в корзине и возможность купить товар")
    def checking_book_in_cart(self, name):
        s(by.text(f"{name}")).should(be.visible)
        browser.element('[data-testid="cart__listDeleteButton"]').should(be.visible)
        browser.element('[data-testid="button__content"]').should(
            have.text("Перейти к покупке")
        )


cart_litres = CartLitres()
