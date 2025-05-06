import os
from pathlib import Path
import allure
import requests
from allure_commons.types import AttachmentType
from dotenv import load_dotenv


# Скриншоты
def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name="screenshot",
        attachment_type=AttachmentType.PNG,
        extension=".png",
    )


# логи
def add_logs(browser):
    log = "".join(f"{text}\n" for text in browser.driver.get_log(log_type="browser"))
    allure.attach(log, "browser_logs", AttachmentType.TEXT, ".log")


# html-код страницы
def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, "page_source", AttachmentType.HTML, ".html")


# скринкаст
def add_video(browser):
    video_url = (
        "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    )
    html = (
        "<html><body><video width='100%' height='100%' controls autoplay><source src='"
        + video_url
        + "' type='video/mp4'></video></body></html>"
    )
    allure.attach(
        html, "video_" + browser.driver.session_id, AttachmentType.HTML, ".html"
    )


# xml страницы
def add_xml(browser):
    xml_dump = browser.driver.page_source
    allure.attach(
        body=xml_dump, name="XML screen", attachment_type=allure.attachment_type.XML
    )

# скринкаст для bstack
def add_bstack_video(session_id):
    load_dotenv(
        dotenv_path=Path(__file__).resolve().parent.parent.parent / f".env.credentials"
    )
    browserstack_session = requests.get(
        url=f"https://api.browserstack.com/app-automate/sessions/{session_id}.json",
        auth=(os.getenv("USER_NAME"), os.getenv("ACCESS_KEY")),
    ).json()
    video_url = browserstack_session["automation_session"]["video_url"]

    allure.attach(
        "<html><body>"
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        "</video>"
        "</body></html>",
        name="video recording",
        attachment_type=allure.attachment_type.HTML,
    )
