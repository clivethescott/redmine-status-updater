import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from auth import login


def submit_logged_time(browser, hours):
    condition = ec.presence_of_element_located((By.ID, "time_entry_hours"))
    time_entry_field = WebDriverWait(browser, 10).until(condition)
    time_entry_field.send_keys(hours)
    activity_dropdown = Select(
        browser.find_element_by_id("time_entry_activity_id"))
    activity_dropdown.select_by_visible_text('Development')
    submit_btn = browser.find_element_by_name('commit')
    submit_btn.click()


def log_time(browser, issue_id, hours):
    url = f"https://apps.mohcc.gov.zw:8084/issues/{issue_id}/time_entries/new"
    login(browser, url)
    submit_logged_time(browser, hours)


def main(args: [str]):
    if len(args) < 2:
        print("Expected issue ID and time taken")
        exit(1)
    issue_id, hours = args[1:]
    browser = webdriver.Firefox()
    try:
        log_time(browser, issue_id, hours)
    finally:
        browser.close()


if __name__ == "__main__":
    main(sys.argv)
