import pickle
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options


opts = Options()
opts.add_argument("start-maximized")
opts.add_experimental_option("excludeSwitches", ['enable-automation'])
opts.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=opts)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

url = 'https://en.onlinesoccermanager.com/'

driver.get(url)

while True:
    try:
        driver.get_window_size()
        if str(driver.current_url).split('/')[-1] == 'Dashboard':
            pickle.dump(driver.get_cookies(), open("cookie.pkl", "wb"))
            print("Completed")
            break
    except exceptions.WebDriverException:
        break



