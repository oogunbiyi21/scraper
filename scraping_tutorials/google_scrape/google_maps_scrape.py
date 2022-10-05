from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from parsel import Selector
import time
import pandas as pd

chromedriver_autoinstaller.install()

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options)

url = 'https://www.google.co.uk/maps/search/co-working+space+near+New+York+City'
driver.get(url)

time.sleep(5)

accept_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Accept all']")
accept_button.click()

time.sleep(10)

page_content = driver.page_source

response = Selector(page_content)

results = []

for el in response.xpath('//div[contains(@aria-label, "Results for")]/div/div[./a]'):
    results.append({
        'link': el.xpath('./a/@href').extract_first(''),
        'title': el.xpath('./a/@aria-label').extract_first('')
    })

results_df = pd.DataFrame(results)
print(results_df)

driver.quit()

