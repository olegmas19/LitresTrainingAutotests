from pathlib import Path
import allure
import pytest
import allure_commons
from dotenv import load_dotenv
from selene import browser, support
import os
from appium import webdriver
from litres_training_autotests.utils.attach import add_screenshot, add_bstack_video, add_xml

@pytest.fixture(scope="session", autouse=True)
def  litres_user():
    load_dotenv()
    litres_login = os.getenv("LITRES_LOGIN")
    litres_password = os.getenv("LITRES_PASSWORD")
    return litres_login, litres_password

def pytest_addoption(parser):
    parser.addoption(
        "--context",
        required=False,
        default="bstack",
        choices=["bstack", "local_emulator"],
    )


def pytest_configure(config):
    context = config.getoption("--context")
    load_dotenv(
        dotenv_path=Path(__file__).resolve().parent.parent.parent / f".env.{context}"
    )

@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope="function", autouse=True)
def android_mobile_management(context):
    from config import config

    options = config.to_driver_options(context=context)

    with allure.step("setup app session"):
        browser.config.driver = webdriver.Remote(
            options.get_capability("remote_url"), options=options
        )

    browser.config.timeout = float(os.getenv("timeout", 15))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    add_screenshot(browser.config)

    add_xml(browser.config)

    session_id = browser.driver.session_id

    with allure.step("tear down app session with id"):
        browser.quit()

    if context == "bstack":
        add_bstack_video(session_id)


