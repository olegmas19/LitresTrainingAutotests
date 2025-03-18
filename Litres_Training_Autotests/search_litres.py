from selene import browser, have, be
import allure
from allure_commons.types import Severity


class SearchLitres:

    def open(self):
        browser.open('/')

    def fill_search(self, value1):
        browser.element('[data-testid="search__input"]').type(value1)

    def click_button_search(self):
        browser.element('[data-testid="search__button"]').click()

    def press_enter_search(self):
        browser.element('[data-testid="search__input"]').press_enter()

    def checking_search_results(self, value1, value2):
        browser.element('[id="pageTitle"]').should(have.text(value1))
        browser.element('[data-testid="art__title"][href="/book/lev-tolstoy/voyna-i-mir-66691848/"]').should(
            have.text(value2))