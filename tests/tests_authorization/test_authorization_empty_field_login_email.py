from Litres_Training_Autotests.authorisation_litres import AuthorisationLitres


def test_checking_authorisation_invalid_data():
    authorisation_litres = AuthorisationLitres()
    #GIVEN
    authorisation_litres.open()

    #WHEN
    authorisation_litres.press_tab_login()
    authorisation_litres.fill_login('')
    authorisation_litres.press_continue()

    #THEN
    authorisation_litres.login_cannot_be_empty('Поле не может быть пустым', 'Продолжить')