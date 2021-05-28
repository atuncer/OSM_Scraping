import pickle
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
import sqlite3

conn = sqlite3.connect('yesir')

opts = Options()
opts.add_argument("start-maximized")
opts.add_experimental_option("excludeSwitches", ['enable-automation'])
opts.add_experimental_option('useAutomationExtension', False)
#opts.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=opts)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

url = 'https://en.onlinesoccermanager.com/'


driver.get(url)

print("asd")
#
# cookies = pickle.load(open("cookies2.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
# time.sleep(2)
#
# driver.get(url)
#
#

while True:
    try:
        driver.get_window_size()
    except exceptions.WebDriverException:
        break

pickle.dump( driver.get_cookies() , open("cookie.pkl","wb"))
print("Completed")

