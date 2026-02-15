from selenium.webdriver.common.by import By


class BasePageUsersLocators:
    def __init__(self):
        self.users_locator = (By.XPATH, "//*[@class='tab-btn active']")
        self.nickname_field_locator = (By.XPATH, "//*[@id='user_nickname']")
        self.first_name_field_locator = (By.XPATH, "//*[@id='user_fname']")
        self.last_name_field_locator = (By.XPATH, "//*[@id='user_lname']")
        self.age_field_locator = (By.XPATH, "//*[@id='user_age']")
        self.job_field_locator = (By.XPATH, "//*[@id='user_job']")
        self.get_user_locator = (By.XPATH, "//*[@onclick='getUser()']")
        self.get_all_button_locator = (By.XPATH, "//*[@onclick='getAllUsers()']")
        self.post_button_locator = (By.XPATH, "//*[@class='btn btn-create']")
        self.update_put_button_locator = (By.XPATH, "//*[@class='btn btn-update']")
        self.delete_button_locator = (By.XPATH, "//*[@class='btn btn-delete']")
        self.status_code_post_locator = (By.XPATH, "//*[contains(text(), 'POST /users') and contains(text(), 'success')]")
        self.response_get_user_tpl = "(//*[contains(text(), 'GET /users/%s')])[last()]"
        self.response_get_users_tpl = "(//*[contains(text(), GET /users/)]"
