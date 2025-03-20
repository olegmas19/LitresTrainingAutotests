<h1> Проект по тестированию сервиса электронных и аудиокниг "Литрес"</h1>

> <a target="_blank" href="https://www.litres.ru">Ссылка на сайт</a>

![This is an image](design/image/litres_page.png)

<h3> Список проверок, реализованных в автотестах:</h3>

### UI-тесты
- [x] Авторизация пользователя на сайте(успешная и неуспешная)
- [x] Поиск по клику кнопки Поиск/по нажатию PressEnter

----
### Проект реализован с использованием:
<img src="design/icons/python-original.svg" width="50"> <img src="design/icons/pytest.png" width="50"> <img src="design/icons/intellij_pycharm.png" width="50"> <img src="design/icons/selene.png" width="50"> <img src="design/icons/selenoid.png" width="50"> <img src="design/icons/jenkins.png" width="50"> <img src="design/icons/allure_report.png" width="50"> <img src="design/icons/allure_testops.png" width="50"> <img src="design/icons/tg.png" width="50"> <img src="design/icons/jira.png" width="50">

----
### Локальный запуск
> Для локального запуска с дефолтными значениями необходимо выполнить команду:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests
```

----
### Удаленный запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/LitresTrainingAutotests/">Ссылка на проект в Jenkins</a>

#### Параметры сборки

* `COMMENT` - комментарий
* `BROWSER_VERSION` - версия браузера


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/LitresTrainingAutotests/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Указать браузер
4. Указать комментарий
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure
7. 
----
### Allure отчет


#### Общие результаты
![This is an image](design/image/allure_report_overview.png)
#### Список тест кейсов
![This is an image](design/image/allure_report1.png)
#### Пример отчета о прохождении ui-теста
![This is an image](design/image/example_test_ui_allure.png)

----

### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1420">Ссылка на проект в Jira</a>

![This is an image](design/image/jira1.png)

----
### Оповещение о результатах прогона тестов в Telegram
![This is an image](design/image/tg_notification.jpeg)
----
### Пример видео прохождения ui-автотеста
![autotest_gif](design/image/autotest.gif)

