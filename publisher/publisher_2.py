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

for link in links:
    link_dict = {}
    try:
        chromedriver_autoinstaller.install()
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        driver = webdriver.Chrome(options=options)
        driver.get(link)

        # Get Logo URL
        try:
            logo = driver.find_element(by=By.ID, value="ctl01_TemplateBody_WebPartManager1_gwpciMiniProfile_ciMiniProfile_contactPicture_profileImage")
            link_dict["logo_url"] = logo.get_attribute("src")
        except NoSuchElementException:
            link_dict["logo_url"] = None

        # Get Company
        try:
            company = driver.find_element(by=By.ID, value="ctl01_TemplateBody_WebPartManager1_gwpciNewContactMiniProfileCommon_ciNewContactMiniProfileCommon_contactName_institute")
            link_dict["company"] = company.get_attribute('textContent')
        except NoSuchElementException:
            link_dict["company"] = None

        # Get Description
        try:
            description = driver.find_element(by=By.ID, value="ctl01_TemplateBody_WebPartManager1_gwpciProfileSection_ciProfileSection_APA_CompanyProfile.CompanyBio")
            link_dict["description"] = description.get_attribute('textContent')
        except NoSuchElementException:
            link_dict["description"] = None

        # Get Email
        try:
            email = driver.find_element(by=By.LINK_TEXT, value="Email")
            link_dict["email"] = email.get_attribute('href').split(":")[1]
        except NoSuchElementException:
            link_dict["email"] = None

        # Get Website
        try:
            website = driver.find_element(by=By.XPATH, value="//*[@id='ctl01_TemplateBody_WebPartManager1_gwpciNewSummaryDisplayCommon_ciNewSummaryDisplayCommon_Website']/a")
            link_dict["website"] = website.get_attribute('href')
            link_dict_list.append(link_dict)
        except NoSuchElementException:
            link_dict["email"] = None

        # Get Social Media
        driver.find_element(by=By.CSS_SELECTOR, value='[aria-controls ="ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_Page_2"]').click()
        time.sleep(15)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.save_screenshot('screenshot.png')

        # Get Twitter
        try:
            twitter = driver.find_element(by=By.XPATH, value="//*[@id='ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_CompanySocial_APA_CompanyProfile.CompanyTwitter']/a")
            link_dict["twitter"] = twitter.get_attribute('href')
        except NoSuchElementException:
            link_dict["twitter"] = None

        # Get Facebook
        try:
            facebook = driver.find_element(by=By.XPATH,
                                          value="//*[@id='ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_CompanySocial_APA_CompanyProfile.CompanyFacebook']/a")
            link_dict["facebook"] = facebook.get_attribute('href')
        except NoSuchElementException:
            link_dict["facebook"] = None

        # Get Instagram
        try:
            instagram = driver.find_element(by=By.XPATH,
                                          value="//*[@id='ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_CompanySocial_APA_CompanyProfile.CompanyInstagram']/a")
            link_dict["instagram"] = instagram.get_attribute('href')
        except NoSuchElementException:
            link_dict["instagram"] = None

        # Get YouTube
        try:
            youtube = driver.find_element(by=By.XPATH,
                                            value="//*[@id='ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_CompanySocial_APA_CompanyProfile.CompanyYouTube']/a")
            link_dict["youtube"] = youtube.get_attribute('href')
        except NoSuchElementException:
            link_dict["youtube"] = None

        # Get LinkedIn
        try:
            linkedin = driver.find_element(by=By.XPATH,
                                          value="//*[@id='ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_CompanySocial_APA_CompanyProfile.CompanyLinkedIn']/a")
            link_dict["linkedin"] = linkedin.get_attribute('href')
        except NoSuchElementException:
            link_dict["linkedin"] = None

        # Get Distribution
        driver.find_element(by=By.CSS_SELECTOR,
                            value='[aria-controls ="ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_Page_3"]').click()
        time.sleep(15)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.save_screenshot('screenshot.png')

        # Get Australian Distributors
        try:
            aus_dist = driver.find_element(by=By.ID,
                                          value="ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_DistributionImprintsandAgencies_APA_CompanyProfile.AustralianDistributors")
            link_dict["aus_dist"] = aus_dist.get_attribute('textContent')
        except NoSuchElementException:
            link_dict["aus_dist"] = None

        # Get Overseas Distributors
        try:
            over_dist = driver.find_element(by=By.ID,
                                          value="ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_DistributionImprintsandAgencies_APA_CompanyProfile.OverseasDistributors")
            link_dict["over_dist"] = over_dist.get_attribute('textContent')
        except NoSuchElementException:
            link_dict["over_dist"] = None

        # Get Major Imprints
        try:
            over_dist = driver.find_element(by=By.ID,
                                            value="ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_DistributionImprintsandAgencies_APA_CompanyProfile.MajorImprints")
            link_dict["over_dist"] = over_dist.get_attribute('textContent')
        except NoSuchElementException:
            link_dict["over_dist"] = None

        # Get Sectors and Services
        driver.find_element(by=By.CSS_SELECTOR,
                            value='[aria-controls ="ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_Page_4"]').click()
        time.sleep(15)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.save_screenshot('screenshot.png')

        # Get Services
        try:
            services = driver.find_element(by=By.ID,
                                            value="ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_SectorandServices_APA_CompanyProfile.IndustryService")
            link_dict["services"] = services.get_attribute('textContent')
        except NoSuchElementException:
            link_dict["services"] = None

        # Get Sectors
        try:
            sectors = driver.find_element(by=By.ID,
                                           value="ctl01_TemplateBody_WebPartManager1_gwpciOrganisationProfile_ciOrganisationProfile_SectorandServices_APA_CompanyProfile.SectorPublishing")
            link_dict["sectors"] = sectors.get_attribute('textContent')
        except NoSuchElementException:
            link_dict["sectors"] = None

        print(link_dict)
        link_dict_list.append(link_dict)

    finally:
        driver.quit()

link_dict_df = pd.DataFrame(link_dict_list).drop_duplicates()
link_dict_df.to_csv("publisher_data.csv", index=False)
print(link_dict_df)
