import time

import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome()
url = "https://www.publishers.asn.au/Web/Web/Directory/Member%20Directory.aspx?hkey=3ffd0619-5e25-409b-95c6-f8ee45dad230"
driver.get(url)


publisher_prompt_id = "ctl01_TemplateBody_WebPartManager1_gwpciNewQueryMenuCommon_ciNewQueryMenuCommon_ResultsGrid_Sheet0_Input1_DropDown1"
submit_button_id = "ctl01_TemplateBody_WebPartManager1_gwpciNewQueryMenuCommon_ciNewQueryMenuCommon_ResultsGrid_Sheet0_SubmitButton"
table_id = "ctl01_TemplateBody_WebPartManager1_gwpciNewQueryMenuCommon_ciNewQueryMenuCommon_ResultsGrid_GridPanel1"
show_all_id = "ctl01_TemplateBody_WebPartManager1_gwpciNewQueryMenuCommon_ciNewQueryMenuCommon_ResultsGrid_Grid1_ctl00_ctl03_ctl01_ShowAll"
table_class = "rgMasterTable CaptionTextInvisible"


select = Select(driver.find_element(by=By.ID, value=publisher_prompt_id))
select.select_by_value('Publisher')
submit_button = driver.find_element(by=By.ID, value=submit_button_id)
submit_button.click()

try:
    element = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.ID, table_id))
    )
    driver.save_screenshot('screenshot.png')
    table_element = driver.find_element(by=By.ID, value=table_id)

    show_all_link = driver.find_element(by=By.ID, value=show_all_id)
    show_all_link.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    driver.save_screenshot('screenshot.png')

    elements = driver.find_elements(by=By.XPATH, value="//table[@class = 'rgMasterTable CaptionTextInvisible']//td/a")
    link_list = []
    for element in elements:
        link_list.append(element.get_attribute("href"))

    print(link_list)

except NoSuchElementException as e:
    print('Did not load page properly: {}'.format(e))

finally:
    driver.quit()

df = pd.DataFrame({"links": link_list})
df.to_csv("links.csv", index=False)


