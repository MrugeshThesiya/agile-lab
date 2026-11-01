from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://www.youtube.com")

search_box = driver.find_element(By.NAME,"search_query")

search_box.send_keys("Selenium Tutorial ")

search_box.send_keys(Keys.RETURN)

time.sleep(3)

driver.save_screenshot("youtube_search_result.png")

driver.quit()
