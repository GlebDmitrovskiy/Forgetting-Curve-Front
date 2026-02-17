from locators.base_page_users_locators import BasePageUsersLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePageUsers:
    def __init__(self, browser):
        self.browser = browser
        self.locators= BasePageUsersLocators()
    def go_to_main_page(self):
        self.browser.get("http://127.0.0.1:8001")

    def find(self, locator):
        return self.browser.find_element(*locator)

    def input_nickname(self, nickname):
        field = self.find(self.locators.nickname_field_locator)
        field.clear()
        self.find(self.locators.nickname_field_locator).send_keys(nickname)

    def input_name(self, name):
        self.find(self.locators.first_name_field_locator).clear()
        self.find(self.locators.first_name_field_locator).send_keys(name)

    def input_last_name(self, lust_name):
        self.find(self.locators.last_name_field_locator).clear()
        self.find(self.locators.last_name_field_locator).send_keys(lust_name)

    def input_age(self, age):
        self.find(self.locators.age_field_locator).clear()
        self.find(self.locators.age_field_locator).send_keys(age)

    def input_job(self, job):
        self.find(self.locators.job_field_locator).clear()
        self.find(self.locators.job_field_locator).send_keys(job)

    def post_user(self, data):
        if data:
            self.input_nickname(data["nickname"])
            self.input_name(data["first_name"])
            self.input_last_name(data["last_name"])
            self.input_age(data["age"])
            self.input_job(data["job"])

        self.find(self.locators.post_button_locator).click()

    def get_user(self):
        self.find(self.locators.get_user_locator).click()

    def delete_user(self, nickname =  None):

        if nickname:
            self.input_nickname(nickname)
        self.find(self.locators.delete_button_locator).click()
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        self.browser.switch_to.alert.accept()
    def get_users(self):
        self.find(self.locators.get_all_button_locator).click()


    def update_user(self):
        self.find(self.locators.update_put_button_locator).click()