from selenium.webdriver.common.by import By
from locators.information_page_locators import InformationPageLocators
from pages.base_page import BasePageUsers
from selenium import webdriver
from pages.information_page import InformationPage
import pytest
from pages.base_page import BasePageUsers
from selenium.webdriver.support.wait import WebDriverWait
from services.functions import text_generator, digit_generator
from selenium.webdriver.support import expected_conditions as EC
import requests
import time


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def base_page(browser):
    return BasePageUsers(browser)


@pytest.fixture
def information_page(browser):
    return InformationPage(browser)


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


@pytest.fixture
def information_factory(information_page, browser, user_factory):
    wait = WebDriverWait(browser, 10)
    data_information = {
        "nickname": user_factory["nickname"],
        "thesis": text_generator(20),
        "explanation": text_generator(10),
    }

    information_page.go_to_information()

    information_page.click_information_button()
    information_page.create_user_information(data_information)


    yield data_information
    try:
        information_page.input_nickname_for_delete(data_information['nickname'])
        information_page.delete_user_information()
    except Exception:
        pass


class TestInformationPage:
    def test_create_user_by_data_information(self, browser, information_page, information_factory, user_factory):
        information_page.go_to_information()
        information_page.click_information_button()
        information_page.input_nickname(information_factory["nickname"])
        information_page.input_thesis(information_factory["thesis"])
        information_page.input_explanation(information_factory["explanation"])
        assert information_factory["nickname"] == information_page.find(information_page.locators.input_nickname_locator).get_attribute("value")
        assert information_factory["thesis"] == information_page.find(information_page.locators.input_thesis_locator).get_attribute("value")
        assert information_factory["explanation"] == information_page.find(information_page.locators.explanation_locator).get_attribute("value")