import sys
from typing import List
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from auth import login


class StatusModifier:

    def __init__(self, browser: webdriver.Firefox, issue_id: str):
        self.browser = browser
        self.issue_id = issue_id
        self.url = f"https://apps.mohcc.gov.zw:8084/issues/{issue_id}"

    def goto_edit_issue(self):
        edit_issue = self.browser.find_element_by_link_text("Edit")
        edit_issue.click()

    def assign_to_self(self):
        assignee = Select(
            self.browser.find_element_by_id("issue_assigned_to_id"))
        assignee.select_by_visible_text("<< me >>")

    def set_status(self, status: str):
        issue_status = Select(
            self.browser.find_element_by_id("issue_status_id"))
        issue_status.select_by_visible_text(status)

    def save(self):
        self.browser.find_element_by_name("commit").click()

    def change_to_status(self, status: str):
        login(self.browser, self.url)

        self.goto_edit_issue()
        self.assign_to_self()
        self.set_status(status)
        # self.save()


def main(args: List[str]) -> None:
    if len(args) < 2:
        print("Expected issue ID and status")
        exit(1)
    issue_id, status = args[1:]
    with webdriver.Firefox() as browser:
        status_modifier = StatusModifier(browser, issue_id)
        status_modifier.change_to_status(status)


if __name__ == "__main__":
    main(sys.argv)
