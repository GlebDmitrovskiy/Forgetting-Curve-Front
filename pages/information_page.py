from locators.information_page_locators import InformationPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class InformationPage:
    def __init__(self, browser):
        self.browser = browser
        self.locators = InformationPageLocators()

    def find(self, locator):
        return self.browser.find_element(*locator)

    def go_to_information(self):
        self.browser.get("http://127.0.0.1:8001/")

    def click_information_button(self):
        wait = WebDriverWait(self.browser, 10)
        element = wait.until(EC.element_to_be_clickable(self.locators.information_button_locator))
        element.click()

    def input_nickname(self, nickname):
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.locators.input_nickname_locator)
        )
        element.clear()
        element.send_keys(nickname)

    def input_thesis(self, thesis):
        self.find(self.locators.input_thesis_locator).send_keys(thesis)

    def input_explanation(self, explanation):
        self.find(self.locators.explanation_locator).send_keys(explanation)

    def input_nickname_for_delete(self, nickname):
        self.find(self.locators.delete_id_user_locator).send_keys(nickname)

    def input_id_for_delete(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.locators.delete_id_user_locator)).get_attribute("value")
        return element

    def create_user_information(self, data: dict):
        if data:
            self.input_nickname(data["nickname"])
            self.input_thesis(data["thesis"])
            self.input_explanation(data["explanation"])
        self.find(self.locators.create_user_information_button_locator).click()

    def get_information(self):
        element = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(self.locators.get_user_information_button_locator))
        element.click()

    def input_delete_user_information(self, nickname):
        input_field = self.find(self.locators.delete_user_nickname_locator)
        input_field.clear()
        input_field.send_keys(nickname)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.locators.delete_id_user_locator)
        )
        WebDriverWait(self.browser, 10).until_not(
            EC.text_to_be_present_in_element_value(self.locators.delete_id_user_locator, "")
        )
        input_field.send_keys(Keys.TAB)
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.locators.delete_user_information)
        )

    def delete_user_information(self):
        self.find(self.locators.delete_user_information).click()
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        self.browser.switch_to.alert.accept()

    def wait_for_delete_data_to_load(self):
        WebDriverWait(self.browser, 20).until_not(
            EC.text_to_be_present_in_element_value(self.locators.delete_id_user_locator, ""),
            message="Данные для удаления (ID) не подтянулись автоматически за 20 секунд"
        )
