
from selenium.webdriver.common.by import By
import time

#Запуск теста производить примерно так: pytest -s -v --language=es Homework3.6\test_items.py
#Тест отрабатывает как в Chrome, так и в Firefox

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items_3_6_10(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    atb = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert atb is not None, "Элемент не найден, попробуйте перезапустить тест"
    time.sleep(20)
