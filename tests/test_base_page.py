from os import waitpid
from time import sleep
from selenium.webdriver.common.by import By
from locators.base_page_users_locators import BasePageUsersLocators
from selenium import webdriver
from pages.base_page import BasePageUsers
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from services.functions import text_generator, digit_generator
from selenium.webdriver.support import expected_conditions as EC
import json


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def base_page(browser):
    return BasePageUsers(browser)


@pytest.fixture
def user_factory(base_page):
    data_user = {
        "nickname": text_generator(10),
        "first_name": text_generator(10),
        "last_name": text_generator(10),
        "age": str(digit_generator(50)),
        "job": text_generator(50)
    }
    base_page.go_to_main_page()
    base_page.post_user(data_user)
    yield data_user
    try:
        base_page.go_to_main_page()
        base_page.delete_user(data_user["nickname"])
    except Exception:
        pass


class TestBasePage:

    def test_create_user_by_factory(self, browser, base_page, user_factory):
        locators = BasePageUsersLocators()
        wait = WebDriverWait(browser, 10)
        base_page.go_to_main_page()
        base_page.input_nickname(user_factory["nickname"])
        base_page.get_user()
        dynamic_xpath = locators.response_get_user_tpl % user_factory["nickname"]
        element = wait.until(EC.visibility_of_element_located((By.XPATH, dynamic_xpath)))
        assert user_factory["nickname"] in element.text
        assert user_factory["first_name"] in element.text
        assert user_factory["last_name"] in element.text
        assert user_factory["age"] in element.text
        assert user_factory["job"] in element.text

    def test_update_user(self, browser, base_page, user_factory):
        wait = WebDriverWait(browser, 10)

        data = {
            "first_name": text_generator(10),
            "last_name": text_generator(10),
            "age": str(digit_generator(50)),
            "job": text_generator(50)
        }
        new_first_name = data["first_name"]
        new_last_name = data["last_name"]
        new_age = data["age"]
        new_job = data["job"]
        locators = BasePageUsersLocators()

        base_page.find(locators.first_name_field_locator).clear()
        base_page.input_name(new_first_name)
        base_page.find(locators.last_name_field_locator).clear()
        base_page.input_last_name(new_last_name)
        base_page.find(locators.age_field_locator).clear()
        base_page.input_age(new_age)
        base_page.find(locators.job_field_locator).clear()
        base_page.input_job(new_job)

        assert new_first_name == base_page.find(locators.first_name_field_locator).get_attribute("value")
        assert new_last_name == base_page.find(locators.last_name_field_locator).get_attribute("value")
        assert new_age == base_page.find(locators.age_field_locator).get_attribute("value")
        assert new_job == base_page.find(locators.job_field_locator).get_attribute("value")
        base_page.update_user()
        base_page.get_user()

    def test_get_user(self, browser, base_page, user_factory):
        locators = BasePageUsersLocators()
        wait = WebDriverWait(browser, 10)
        base_page.input_nickname(user_factory["nickname"])
        base_page.get_user()
        dynamic_xpath = locators.response_get_user_tpl % user_factory["nickname"]
        element = wait.until(EC.visibility_of_element_located((By.XPATH, dynamic_xpath)))
        assert user_factory["nickname"] in element.text
        assert user_factory["first_name"] in element.text
        assert user_factory["last_name"] in element.text
        assert user_factory["age"] in element.text
        assert user_factory["job"] in element.text

    def test_all_users(self, browser, base_page, user_factory):
        wait = WebDriverWait(browser, 10)
        base_page.input_nickname(user_factory["nickname"])
        base_page.get_users()
        wait.until(EC.text_to_be_present_in_element((By.ID, "log"), "GET /users"))
        log_text = browser.find_element(By.ID, "log").text
        assert "GET /users" in log_text

    def test_delete_user(self, browser, base_page, user_factory):
        wait = WebDriverWait(browser, 10)
        base_page.input_nickname(user_factory["nickname"])
        base_page.get_user()
        base_page.delete_user(user_factory["nickname"])
        wait.until(EC.text_to_be_present_in_element((By.ID, "log"), "DELETE /users"))
        log_text = browser.find_element(By.ID, "log").text
        assert "DELETE /users" in log_text