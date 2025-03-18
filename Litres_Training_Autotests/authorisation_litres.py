from selene import browser, have, be
import allure
from allure_commons.types import Severity

class AuthorisationLitres:


    def open(self):
        browser.open('/')

    def press_tab_login(self):
        browser.element('#tab-login').click()

    def fill_login(self, value):
        browser.element('#auth__input--enterEmailOrLogin').type(value)

    def press_continue(self):
        browser.element('[data-testid="auth__button--continue"]').click()

    def fill_password(self, value):
        browser.element('[data-testid="auth__input--enterPassword"]').type(value)

    def press_enter(self):
        browser.element('[data-testid="auth__button--enter"]').click()

    def personal_account_entrance(self):
        browser.element('[data-testid="user-button"]').click()

    def should_have_authorized(self, value1, value2):
        browser.element('[data-testid="profile__userNameMain"]').should(have.text(value1))
        browser.element('[data-testid="profile__logout--button"]').should(have.text(value2))

    def should_not_have_authorized(self, value1, value2, value3):
        browser.element('[data-testid="authorization-popup"]').should(be.visible)
        browser.element('[data-testid="auth__title"]').should(have.text(value1))
        browser.element('[data-testid="textbox--input__error"]').should(have.text(value2))
        browser.element('[data-testid="auth__button--enter"]').should(have.text(value3))

    def login_cannot_be_empty(self, value1, value2):
        browser.element('[data-testid="authorization-popup"]').should(be.visible)
        browser.element('[data-testid="textbox--input__error"]').should(have.text(value1))
        browser.element('[data-testid="auth__button--continue"]').should(have.text(value2))





