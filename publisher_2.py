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

df = pd.read_csv("links.csv")

links = df["links"].tolist()
link_dict_list = []

for link in links[:1]:
    link_dict = {}
    try:
        chromedriver_autoinstaller.install()
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        driver = webdriver.Chrome(options=options)
        driver.get(link)

        # Get Logo URL
        logo = driver.find_element(by=By.ID, value="ctl01_TemplateBody_WebPartManager1_gwpciMiniProfile_ciMiniProfile_contactPicture_profileImage")
        link_dict["logo_url"] = logo.get_attribute("src")

        # Get Company
        company = driver.find_element(by=By.ID, value="ctl01_TemplateBody_WebPartManager1_gwpciNewContactMiniProfileCommon_ciNewContactMiniProfileCommon_contactName_institute")
        link_dict["company"] = company.get_attribute('textContent')

        # Get Description
        description = driver.find_element(by=By.ID, value="ctl01_TemplateBody_WebPartManager1_gwpciProfileSection_ciProfileSection_APA_CompanyProfile.CompanyBio")
        link_dict["description"] = description.get_attribute('textContent')

        # Get Email
        email = driver.find_element(by=By.LINK_TEXT, value="Email")
        link_dict["email"] = email.get_attribute('href').split(":")[1]

        # Get Website
        website = driver.find_element(by=By.XPATH, value="//*[@id='ctl01_TemplateBody_WebPartManager1_gwpciNewSummaryDisplayCommon_ciNewSummaryDisplayCommon_Website']/a")
        link_dict["website"] = website.get_attribute('href')
        link_dict_list.append(link_dict)

        # Get
    finally:
        driver.quit()

print(link_dict_list)
