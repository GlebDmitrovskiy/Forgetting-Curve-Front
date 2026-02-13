from services.functions import text_generator, digit_generator
from selenium import webdriver
from locators.base_page_users_locators import BasePageUsersLocators

base_page= BasePageUsersLocators()


class BasePageUsers:
    def __init__(self, browser):
        self.browser = browser
        self.locators= BasePageUsersLocators()
    def go_to_main_page(self):
        self.browser.get("http://127.0.0.1:8001")

    def find(self, locator):
        return self.browser.find_element(*locator)

    def input_nickname(self, nickname):
        self.find(self.locators.nickname_field_locator).send_keys(nickname)

    def input_name(self, name):
        self.find(self.locators.first_name_field_locator).send_keys(name)

    def input_lust_name(self, lust_name):
        self.find(self.locators.lust_name_field_locator).send_keys(lust_name)

    def input_age(self, age):
        self.find(self.locators.age_field_locator).send_keys(age)

    def input_job(self, job):
        self.find(self.locators.job_field_locator).send_keys(job)

    def post_user(self):
        self.find(self.locators.post_button_locator).click()

    def get_user(self):
        self.find(self.locators.get_user_locator).click()

    def delete_user(self):
        self.find(self.locators.delete_button_locator).click()

    def get_users(self):
        self.find(self.locators.get_all_button_locator).click()
        self.browser.switch_to.alert.accept()

    def update_user(self):
        self.find(self.locators.update_put_button_locator).click()