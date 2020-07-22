import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def login(browser, username: str, password: str):
    condition = ec.presence_of_element_located((By.ID, "username"))
    username = WebDriverWait(browser, 10).until(condition)
    username.send_keys(username)


def open_issue_page(browser, url: str):
    browser.get(url)
    login(browser, "clive", "test")


def load_issue_page(browser, issue_id: int):
    url = f"https://apps.mohcc.gov.zw:8084/issues/{issue_id}"
    open_issue_page(browser, url)


def main(args: [str]):
    browser = webdriver.Firefox()
    issue_id = int(args[1])
    load_issue_page(browser, issue_id)


if __name__ == "__main__":
    main(sys.argv)
