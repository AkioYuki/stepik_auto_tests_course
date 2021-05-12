import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
link = "http://suninjuly.github.io/cats.html"

try:
    browser.find_element_by_id("button")

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
