from selenium.webdriver.common.by import By

class InformationPageLocators:
    def __init__(self):
        self.information_button_locator = (By.XPATH, "//*[@onclick=\"switchTab('info')\"]")
        self.input_nickname_locator = (By.XPATH, "//*[@id = 'info_user_nickname']")
        self.input_thesis_locator = (By.XPATH, "//*[@id = 'info_thesis']")
        self.explanation_locator = (By.XPATH, "//*[@id = 'info_explanation']")
        self.delete_user_nickname_locator = (By.XPATH, "//*[@id = 'delete_user_nickname']")
        self.delete_id_user_locator = (By.XPATH, "//*[@id = 'info_id_to_delete']")
        self.create_user_information_button_locator = (By.XPATH, "//*[@onclick = 'postInformation()']")
        self.get_user_information_button_locator = (By.XPATH, "//*[@onclick = 'getInformation()']")
        self.delete_button_information_user_locator = (By.XPATH, "//*[@class = 'btn btn-delete']")
        self.response_get_user_information_tpl = "(//*[contains(text(), 'GET /users/%s/information')])[last()]"
        self.delete_user_information = (By.XPATH, "//*[@onclick = 'deleteInformation()']")
