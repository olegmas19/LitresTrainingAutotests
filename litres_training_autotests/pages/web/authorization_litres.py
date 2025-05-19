from selene import browser, have, be
import allure


class AuthorizationLitres:

    @allure.step("Открытие сайта 'Литрес'")
    def open(self):
        browser.open("/")

    @allure.step("Нажатие кнопки логина")
    def press_tab_login(self):
        browser.element("#tab-login").click()

    @allure.step("Ввод логина")
    def fill_login(self, value):
        browser.element("#auth__input--enterEmailOrLogin").type(value)

    @allure.step("Нажатие кнопки 'Продолжить'")
    def press_continue(self):
        browser.element('[data-testid="auth__button--continue"]').click()

    @allure.step("Ввод пароля")
    def fill_password(self, value):
        browser.element('[data-testid="auth__input--enterPassword"]').type(value)

    @allure.step("Нажатие кнопки 'Войти'")
    def press_enter(self):
        browser.element('[data-testid="auth__button--enter"]').click()

    @allure.step("Открытие страницы с профилем")
    def personal_account_entrance(self):
        browser.open("https://www.litres.ru/me/profile/")

    @allure.step("Проверка успешной авторизации с валидными данными")
    def should_have_authorized(self, value1, value2):
        browser.element('[data-testid="profile__userNameMain"]').should(
            have.text(value1)
        )
        browser.element('[data-testid="profile__logout--button"]').should(
            have.text(value2)
        )

    @allure.step("Проверка неуспешной авторизации с невалидными данными")
    def should_not_have_authorized(self, value1, value2, value3):
        browser.element('[data-testid="authorization-popup"]').should(be.visible)
        browser.element('[data-testid="auth__title"]').should(have.text(value1))
        browser.element('[data-testid="textbox--input__error"]').should(
            have.text(value2)
        )
        browser.element('[data-testid="auth__button--enter"]').should(have.text(value3))

    @allure.step("Проверка неуспешной авторизация/пустое поле 'почта или логин'")
    def login_cannot_be_empty(self, value1, value2):
        browser.element('[data-testid="authorization-popup"]').should(be.visible)
        browser.element('[data-testid="textbox--input__error"]').should(
            have.text(value1)
        )
        browser.element('[data-testid="auth__button--continue"]').should(
            have.text(value2)
        )


authorization_litres = AuthorizationLitres()
