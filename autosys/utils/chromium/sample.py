import time

from selenium import webdriver

_chrome_driver: str = "/path/to/chromedriver"  # Optional argument, if not specified will search path.
_chrome_driver = ""
driver = webdriver.Chrome(_chrome_driver)
driver.get("http://www.google.com/")
time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name("q")
search_box.send_keys("ChromeDriver")
search_box.submit()
time.sleep(5)  # Let the user actually see something!
while True:
    time.sleep(100)
# driver.quit()
