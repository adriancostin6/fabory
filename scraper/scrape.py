#!/usr/bin/env python
import login
import constants as const 
from selenium import webdriver

def scrape():
    pass

def main():
    try:
        username, password = login.credentials()

        driver = webdriver.Chrome()
        login.login(username, password, driver)

        while(True):
            pass
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()
