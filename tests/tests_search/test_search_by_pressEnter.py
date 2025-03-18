from selene import browser, have, be

from Litres_Training_Autotests.search_litres import SearchLitres


def test_search_press_enter_audio_author():
    search_litres = SearchLitres()
    # GIVEN
    search_litres.open()

    # WHEN
    search_litres.fill_search("Война и мир")
    search_litres.press_enter_search()

    # THEN
    search_litres.checking_search_results('Результаты поиска «Война и мир»', 'Война и мир')

