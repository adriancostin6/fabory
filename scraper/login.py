import getpass as gp
import constants as const
from typing import Tuple
from selenium import webdriver
from selenium.webdriver.common.utils import Keys
from selenium.webdriver.remote.webdriver import WebElement

def credentials() -> Tuple[str, str]:
    username = input('Username:')
    try:
        password = gp.getpass();
        return username, password
    except (gp.GetPassWarning, EOFError) as e:
        raise e

def login_elements(driver: webdriver.Chrome) -> Tuple[WebElement, WebElement]:
    driver.get(const.URL_LOGIN_PAGE)

    userfield = driver.find_element('xpath', const.XPATH_LOGIN_USERNAME)
    passfield = driver.find_element('xpath', const.XPATH_LOGIN_PASSWORD)

    return userfield, passfield

def login(username: str, password: str, driver: webdriver.Chrome):
    userfield, passfield = login_elements(driver)

    userfield.send_keys(username)
    passfield.send_keys(password)
    passfield.send_keys(Keys.RETURN)
