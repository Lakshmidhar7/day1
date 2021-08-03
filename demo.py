from selenium import webdriver

import time

browser = webdriver.Chrome('I:\chromedriver_win32/chromedriver.exe')

browser.get('https://www.youtube.com/')
print(browser.title)


try:
    assert "Facebook" == browser.title
except AssertionError:
    print(f"page title not matched {browser.title} experted title is{'YouTube'}")

browser.minimize_window()
time.sleep(2)
browser.maximize_window()
time.sleep(2)
browser.close()
