from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wpm = int(input("How much WPM do you want (capped at 401)?\n"))
x = 1

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://10fastfingers.com/typing-test/english")

cookiesButton = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')))
cookiesButton.click()
time.sleep(3)

while x <= wpm:
    word = driver.find_element_by_xpath('//*[@id="row1"]/span[' + str(x) + ']').text
    driver.find_element_by_id('inputfield').send_keys(str(word) + Keys.SPACE)
    x += 1


'''
wordList = [driver.find_elements_by_xpath('//*[@id="row1"]')]

for element in wordList:
    print(element)
    print(element.text)

for p in range(len(wordList)):
    print(wordList[p])
'''
