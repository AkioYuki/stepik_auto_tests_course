import math
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)
    price = browser.find_element_by_id('price').text
    my_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element(
            (By.ID, "price"), "$100")
    )
    book = browser.find_element_by_id('book')
    book.click()
    x = int(browser.find_element_by_id('input_value').text)
    my_answer = calc(x)
    browser.find_element_by_id('answer').send_keys(my_answer)
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
