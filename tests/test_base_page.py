from time import sleep
from locators.base_page_users_locators import BasePageUsersLocators
from selenium import webdriver
from pages.base_page import BasePageUsers
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from services.functions import text_generator, digit_generator
import json


class TestBasePage:

    def test_base_page(self):
        browser = webdriver.Chrome()
        wait = WebDriverWait(browser, 10)
        locators = BasePageUsersLocators()
        base_page = BasePageUsers(browser)
        my_nickname = text_generator(10)
        my_name = text_generator(10)
        my_lust_name = text_generator(10)
        my_age = str(digit_generator(50))
        my_job = text_generator(50)
        wait = WebDriverWait(browser, 10)
        base_page.go_to_main_page()
        base_page.input_nickname(my_nickname)
        assert my_nickname == base_page.find(locators.nickname_field_locator).get_attribute("value")
        base_page.input_name(my_name)
        assert my_name == base_page.find(locators.first_name_field_locator).get_attribute("value")
        base_page.input_lust_name(my_lust_name)
        assert my_lust_name == base_page.find(locators.lust_name_field_locator).get_attribute("value")
        base_page.input_age(my_age)
        assert my_age == base_page.find(locators.age_field_locator).get_attribute("value")
        base_page.input_job(my_job)
        assert my_job == base_page.find(locators.job_field_locator).get_attribute("value")
        base_page.post_user()
        element = wait.until(EC.visibility_of_element_located(locators.status_code_post_locator))
        response_post = element.text
        assert "POST /users" in response_post
        assert '"status": "success"' in response_post
        base_page.find(locators.nickname_field_locator).clear()
        base_page.input_nickname(my_nickname)
        base_page.update_user()
        base_page.post_user()
        assert my_nickname == base_page.find(locators.nickname_field_locator).get_attribute("value")
        data = {
            "nickname": text_generator(10),
            "first_name": text_generator(10),
            "last_name": text_generator(10),
            "age": digit_generator(50),
            "job": text_generator(50)
        }
        base_page.find(locators.nickname_field_locator).clear()
        base_page.input_nickname(data["nickname"])
        base_page.find(locators.first_name_field_locator).clear()
        base_page.input_name(data["first_name"])
        base_page.find(locators.lust_name_field_locator).clear()
        base_page.input_lust_name(data["last_name"])
        base_page.find(locators.age_field_locator).clear()
        base_page.input_age(data["age"])
        base_page.find(locators.job_field_locator).clear()
        base_page.input_job(data["job"])
        base_page.update_user()
        base_page.post_user()
        base_page.get_user()
        """Доделать гет и удаление"""
        #element = wait.until(EC.visibility_of_element_located((locators.response_get))).text.split("→")
        #json_element = json.loads(element[1])
        #print(json_element)
        #assert data["nickname"] == json_element[-1]["nickname"]
        #assert data["first_name"] == json_element[-1]["first_name"]
        #assert data["last_name"] == json_element[-1]["last_name"]
        #assert data["age"] == json_element[-1]["age"]
        #assert data["job"] == json_element[-1]["job"]
        browser.quit()
