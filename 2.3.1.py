import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element_by_id('input_value').text)
    my_answer = calc(x)
    browser.find_element_by_id('answer').send_keys(my_answer)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()






finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
