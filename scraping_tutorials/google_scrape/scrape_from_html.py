from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import time
import pandas as pd

chromedriver_autoinstaller.install()

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options)

url = 'http://localhost:63342/PyCharm%20Projects/scraper/scraping_tutorials/google_scrape/bham_cowork.html?_ijt=nsupmluorlnpb3m9h9md7su978'
driver.get(url)


time.sleep(5)

final_list = []

elements_list = driver.find_elements(by=By.XPATH, value='//div[contains(@aria-label, "Results for")]/div/div[./a]')
for element in elements_list:
    elements_dict = {}
    html = element.get_attribute('innerHTML')
    print(html)
    soup = BeautifulSoup(html, "html.parser")
    try:
        elements_dict["title"] = soup.find("a", class_="hfpxzc")["aria-label"]
        elements_dict["link"] = soup.find("a", class_="lcr4fd S9kvJb")["href"]
    except Exception as e:
        print(e)
        continue
    final_list.append(elements_dict)

print(final_list)

results_df = pd.DataFrame(final_list)
results_df.to_csv("birmingham_links.csv")

driver.quit()

