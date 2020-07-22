import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv


def get_auth():
    load_dotenv()
    username = os.getenv("REDMINE_USER")
    password = os.getenv("REDMINE_PASS")
    return (username, password)


def login(browser, url):
    browser.get(url)
    username, password = get_auth()

    condition = ec.presence_of_element_located((By.ID, "username"))
    username_field = WebDriverWait(browser, 10).until(condition)
    username_field.send_keys(username)
    password_field = browser.find_element_by_id("password")
    password_field.send_keys(password)
    login_btn = browser.find_element_by_id("login-submit")
    login_btn.click()
    condition = ec.presence_of_element_located((By.ID, "username"))
