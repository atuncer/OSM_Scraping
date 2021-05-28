import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('identifier.sqlite')

opts = Options()
opts.add_argument("start-maximized")
opts.add_experimental_option("excludeSwitches", ['enable-automation'])
opts.add_experimental_option('useAutomationExtension', False)
#opts.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=opts)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

url = 'https://en.onlinesoccermanager.com/LeagueTypes/'


driver.get(url)
cookies = pickle.load(open("cookie.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)


# time.sleep(20)
# pickle.dump( driver.get_cookies() , open("cookie.pkl","wb"))

time.sleep(5)
driver.get(url)
time.sleep(5)

table = driver.find_element_by_xpath('//*[@id="leaguetypes-table"]/tbody')
lent = len(table.find_elements_by_xpath(".//tr"))
pickle.dump(driver.get_cookies() , open("cookie.pkl","wb"))

league,team = "",""
flag = 0
for i in range(lent):  # all leagues
    row = driver.find_element_by_xpath(f'/html/body/div[3]/div[4]/div/div/div/div/div[2]/div/div/div/div/table/tbody/tr[{i+1}]')
    league = row.find_element_by_xpath('.//td[1]/span').text
    row.click()
    time.sleep(3)
    lent2 = len(driver.find_element_by_xpath('//*[@id="leaguetypes-table"]/tbody').find_elements_by_xpath(".//tr"))
    pickle.dump(driver.get_cookies(), open("cookie.pkl", "wb"))
    for j in range(flag,lent2):  # teams in that league
        flag = 0
        row2 = driver.find_element_by_xpath(f"/html/body/div[3]/div[4]/div/div/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr[{j+1}]")
        team = row2.find_element_by_xpath('.//td[1]/span').text
        row2.click()
        time.sleep(3)

        for l in range(4):  # positions in that team
            for k in range(len(driver.find_element_by_xpath(f'//*[@id="body-content"]/div/div[1]/div[2]/div/div/div/div/table/tbody[{l+1}]').find_elements_by_xpath(".//tr"))):  # players
                plr = []
                plr.append(str(driver.find_element_by_xpath(f"/html/body/div[3]/div[4]/div/div/div/div[1]/div[2]/div/div/div/div/table/tbody[{l+1}]/tr[{k+1}]/td[1]/span").text).replace('\'',' '))
                plr.append(driver.find_element_by_xpath(f"/html/body/div[3]/div[4]/div/div/div/div[1]/div[2]/div/div/div/div/table/tbody[{l+1}]/tr[{k+1}]/td[2]").text)
                plr.append(driver.find_element_by_xpath(f"/html/body/div[3]/div[4]/div/div/div/div[1]/div[2]/div/div/div/div/table/tbody[{l+1}]/tr[{k+1}]/td[3]").text)
                plr.append(str(driver.find_element_by_xpath(f"/html/body/div[3]/div[4]/div/div/div/div[1]/div[2]/div/div/div/div/table/tbody[{l+1}]/tr[{k+1}]/td[4]/span").get_attribute('title')).replace('\'',' '))
                plr.append(driver.find_element_by_xpath(f"/html/body/div[3]/div[4]/div/div/div/div[1]/div[2]/div/div/div/div/table/tbody[{l + 1}]/tr[{k + 1}]/td[6]").text)
                plr.append(driver.find_element_by_xpath(f"/html/body/div[3]/div[4]/div/div/div/div[1]/div[2]/div/div/div/div/table/tbody[{l + 1}]/tr[{k + 1}]/td[7]").text)
                plr.append(driver.find_element_by_xpath(f"/html/body/div[3]/div[4]/div/div/div/div[1]/div[2]/div/div/div/div/table/tbody[{l + 1}]/tr[{k + 1}]/td[8]").text)
                plr.append(str(league).replace('\n',' '))
                plr.append(str(team).replace('\n',' '))
                plr.append(driver.find_element_by_xpath(f"/html/body/div[3]/div[4]/div/div/div/div[1]/div[2]/div/div/div/div/table/tbody[{l + 1}]/tr[{k + 1}]/td[11]/bdi/span/span[2]").text)

                cmd = f"INSERT INTO players VALUES ('{plr[0]}','{plr[1]}',{plr[2]},'{plr[3]}',{plr[4]},{plr[5]},{plr[6]},'{plr[7]}','{plr[8]}','{plr[9]}')"
                print(cmd,i,j)
                try:
                    conn.cursor().execute(cmd)
                except Error:
                    print('error')
                    conn.rollback()
            conn.commit()

        driver.execute_script("window.history.go(-1)")
        time.sleep(3)
    driver.execute_script("window.history.go(-1)")
    time.sleep(3)