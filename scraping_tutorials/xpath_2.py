from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options)
driver.get("https://news.ycombinator.com/newest")

articles = []

for i in range(0, 3):
    elems = driver.find_elements(by=By.XPATH, value="//a[@class='titlelink'][starts-with(text(), 'Ask HN')]/../..")

for elem in elems:
    link = elem.find_element(by=By.XPATH, value=".//a[@class='titlelink']")
    articles.append({
    "id": elem.get_attribute("id"),
    "link": link.get_attribute("href"),
    "title": link.text
    })

next = driver.find_element(by=By.XPATH, value="//a[@rel='next']")
next.click()

print(articles)

driver.quit()