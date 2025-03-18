from Litres_Training_Autotests.search_litres import SearchLitres


def test_search_click_book_author():
    search_litres = SearchLitres()

    # GIVEN
    search_litres.open()

    # WHEN
    search_litres.fill_search('Война и мир')
    search_litres.click_button_search()

    # THEN
    search_litres.checking_search_results('Результаты поиска «Война и мир»', 'Война и мир')


