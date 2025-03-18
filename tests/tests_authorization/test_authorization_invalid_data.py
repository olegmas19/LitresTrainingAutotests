from Litres_Training_Autotests.authorisation_litres import AuthorisationLitres


def test_checking_authorisation_invalid_data():
    authorisation_litres = AuthorisationLitres()
    #GIVEN
    authorisation_litres.open()

    #WHEN
    authorisation_litres.press_tab_login()
    authorisation_litres.fill_login('qweasdzxc')
    authorisation_litres.press_continue()
    authorisation_litres.fill_password('qweasdzxc')
    authorisation_litres.press_enter()

    #THEN
    authorisation_litres.should_not_have_authorized('Ввести пароль', 'Неверное сочетание логина и пароля', 'Войти')

