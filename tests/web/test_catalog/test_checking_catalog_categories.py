from allure_commons.types import Severity
import allure
from litres_training_autotests.page.web.catalog_litres import catalog_litres


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "KING_PLANES")
@allure.feature("Каталог")
@allure.story("Пользователь может просмотреть все категории каталога")
@allure.description("Простые тесты на проверку категорий каталога")
@allure.suite("UI-Тесты")
@allure.link("https://www.litres.ru/", name="Testing")
@allure.title("Проверка наличия категорий в каталоге")
def test_checking_catalog_categories():

    # GIVEN
    catalog_litres.open()

    # WHEN
    catalog_litres.go_to_catalog()

    # THEN
    catalog_litres.check_texts_on_page(
        "Легкое чтение",
        "Серьезное чтение",
        "История",
        "Знания и навыки",
        "Психология, мотивация",
        "Спорт, здоровье, красота",
        "Хобби, досуг",
        "Дом, дача",
        "Детские книги",
        "Родителям",
        "Публицистика и периодические издания",
        "Зарубежная литература",
        "Комиксы и манга",
        "Эксклюзивы",
        "Черновики",
        "Фанфики",
        "Бесплатные книги",
    )
