import allure
from allure_commons.types import Severity
from litres_training_autotests.page.web.cart_litres import cart_litres


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "KING_PLANES")
@allure.feature("Корзина")
@allure.story("Пользователь может добавить товар в корзину")
@allure.description("Простые тесты на проверку категорий корзины")
@allure.suite("UI-Тесты")
@allure.link("https://www.litres.ru/", name="Testing")
@allure.title("Проверка добавления товара в корзину")
def test_add_to_cart():

    # GIVEN
    cart_litres.open("/book/sergey-lukyanenko/sedmoy-71899996/")

    # WHEN
    cart_litres.add_book_to_card()
    cart_litres.close_modal_window()
    cart_litres.go_to_cart()

    # THEN
    cart_litres.checking_book_in_cart("Седьмой")
