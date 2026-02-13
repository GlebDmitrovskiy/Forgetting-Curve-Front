from selenium.webdriver.common.by import By


class BasePageUsersLocators:
    def __init__(self):
        self.users_locator = (By.XPATH, "//*[@class='tab-btn active']")
        self.nickname_field_locator = (By.XPATH, "//*[@id='user_nickname']")
        self.first_name_field_locator = (By.XPATH, "//*[@id='user_fname']")
        self.lust_name_field_locator = (By.XPATH, "//*[@id='user_lname']")
        self.age_field_locator = (By.XPATH, "//*[@id='user_age']")
        self.job_field_locator = (By.XPATH, "//*[@id='user_job']")
        self.get_user_locator = (By.XPATH, "//*[@onclick='getUser()']")
        self.get_all_button_locator = (By.XPATH, "//*[@onclick='getAllUsers()']")
        self.post_button_locator = (By.XPATH, "//*[@class='btn btn-create']")
        self.update_put_button_locator = (By.XPATH, "//*[@class='btn btn-update']")
        self.delete_button_locator = (By.XPATH, "//*[@class='btn btn-delete']")
        self.status_code_post_locator = (By.XPATH, "//*[contains(text(), 'POST /users') and contains(text(), 'success')]")
        #self.response_get = (By.XPATH, "//*[contains (text(), 'GET /users/[-1]')]")
        """Доделать локатор для поиска словоря гета чтобы сравнить"""