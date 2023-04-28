import time
# from selenium import webdriver
# import pytest
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)


def test_check_page_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


# def test_fill_search_city_field(driver):
#     driver.get('https://openweathermap.org/')
#     search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
#     search_city_field.send_keys('New York')
#     time.sleep(5)
#     search_button = driver.find_element(By.CSS_SELECTOR, "button[class='button-round dark']")
#     search_button.click()
#     driver.implicitly_wait(2)
#     search_option = driver.find_element(By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")
#     search_option.click()
#     expected_city = 'New York City, US'
#     time.sleep(3)
#     displayed_city = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#         (By.CSS_SELECTOR, ".grid-container.grid-4-5 h2")))
#     displayed_city_text = displayed_city.text
#     print(displayed_city_text)
#     assert displayed_city_text == expected_city

def test_fill_search_city_field(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('New York')
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
    search_option.click()
    expected_city = 'New York City, US'
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'New York'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city
