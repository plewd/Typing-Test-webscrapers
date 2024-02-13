from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

loops = 1000
x = 0

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://loki.katto.studio/#")

# MAIN CODE
# time.sleep at 0.025 works (sometimes)
# use explicit waits (https://www.selenium.dev/documentation/webdriver/waits/)

while x <= loops:
    time.sleep(0.1)
    try:
        word = driver.find_element_by_xpath('//*[@id="row-' + str(x) + '"]').text
        driver.find_element_by_tag_name('body').send_keys(str(word) + Keys.SPACE)
    except:
        pass
    else:
        x += 1



'''
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


FANCY WAIT FOR ELEMENT TO APPEAR CODE -- DOES NOT WORK

while x <= wpm:
    my_element_xpath = '//*[@id="row-' + str(x) + '"]'
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    word = WebDriverWait(driver, 3, ignored_exceptions=ignored_exceptions) \
        .until(expected_conditions.presence_of_element_located((By.XPATH, my_element_xpath)))
    driver.find_element_by_tag_name('body').send_keys(str(word) + Keys.SPACE)
    x += 1


TEST CODE TO FIND MULTIPLE ELEMENTS AT A TIME

while x <= wpm:
    classWord = driver.find_elements_by_class_name("row")
    for i in classWord:
        i.text
    print(classWord)
    time.sleep(0.5)
    driver.find_element_by_tag_name('body').send_keys(str(classWord) + Keys.SPACE)
    x += 1
'''
