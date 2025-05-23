from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()  
driver.maximize_window()
wait = WebDriverWait(driver, 10)
url = "https://localhost:2443" 

# Тест 1: Успешная авторизация
def test_successful_login():
    driver.get(url)
    time.sleep(10)
    driver.find_element(By.ID, "username").send_keys("root")
    driver.find_element(By.ID, "password").send_keys("0penBmc")
    
    #login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test-id="login-button-submit"]')))
    #login_btn.click()
    
    driver.find_element(By.CSS_SELECTOR, '[data-test-id="login-button-submit"]').click()

    time.sleep(5)
    try:
        assert "#" in driver.page_source
        print("✅ Тест успешной авторизации прошел")
    except AssertionError:
        print("❌ Тест успешной авторизации провален")

# Тест 2: Неверные данные
# def test_wrong_credentials():
#     driver.get(url)
#     time.sleep(10)
#     driver.find_element(By.ID, "username").send_keys("wronguser")
#     driver.find_element(By.ID, "password").send_keys("wrongpass")
#     driver.find_element(By.CSS_SELECTOR, '[data-test-id="login-button-submit"]').click()
#     time.sleep(5)
    
#     try:
#         #error = driver.find_element(By.CLASS_NAME, "login-error")
#         assert "login" in driver.page_source
#         print("✅ Тест неверных данных прошел")
#     except AssertionError:
#         print("❌ Тест неверных данных провален")

# Тест 3: Блокировка учетной записи
# def test_account_lockout():
#     driver.get(url)
#     time.sleep(5)
#     for i in range(3):
#         driver.find_element(By.ID, "username").send_keys("root")
#         driver.find_element(By.ID, "password").send_keys("pass")
#         driver.find_element(By.CSS_SELECTOR, '[data-test-id="login-button-submit"]').click()
#         time.sleep(5)
#         driver.refresh()
        
#     try:
#         error = driver.find_element(By.CLASS_NAME, "invalid-feedback")
#         assert "locked" in error.text.lower()
#         print("✅ Тест блокировки аккаунта прошел")
#     except:
#         print("❌ Тест блокировки аккаунта провален")

test_successful_login()
#test_wrong_credentials()
#test_account_lockout()

driver.quit()
