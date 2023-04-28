from selenium.webdriver.common.by import By
import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# def test_open():
#     browser.get('http://suninjuly.github.io/xpath_examples')
#     time.sleep(5)

# def test_open_2():
#     browser.get('http://suninjuly.github.io/cats.html')
#     bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")
#     print(bullet_cat.text)
#
# def test_view():
#     browser.get('http://suninjuly.github.io/cats.html')
#     view_buttons = browser.find_elements(By.XPATH, "//*[contains(text(), 'View')]")
#     print(view_buttons)
#     assert len(view_buttons) == 6, 'Wrong length'

# def open_page():
#     browser.get('http://suninjuly.github.io/cats.html')
#     bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")
#     print(bullet_cat.text)
#     view_buttons = browser.find_elements(By.XPATH, "//*[contains(text(), 'View')]")
#     assert len(view_buttons) == 6, 'Wrong length'
#
#
# def test_open_page():
#     open_page()
