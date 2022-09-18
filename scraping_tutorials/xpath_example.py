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
driver.get("https://www.amazon.com/Dyson-V10-Allergy-Cordless-Cleaner/dp/B095LD5SWQ/")

title = driver.find_element(by=By.XPATH, value='//span[@id="productTitle"]')
image = driver.find_element(by=By.XPATH, value='//div[@id="imgTagWrapperId"]/img')

product_data = {
'title': title.text,
'image_url': image.get_attribute('src')
}

print(product_data)
driver.quit()


def autologin(driver, url, username, password):
    # Load the page
    driver.get(url)

    # Find a password input field and enter the specified password string
    password_input = driver.find_element(by=By.XPATH, value="//input[@type='password']")
    password_input.send_keys(password)

    # Find a visible input field preceding out password field and enter the specified username
    username_input = password_input.find_element(by=By.XPATH, value=".//preceding::input[not(@type='hidden')]")
    username_input.send_keys(username)

    # Find the form element enclosing our password field
    form_element = password_input.find_element(by=By.XPATH, value=".//ancestor::form")

    # Find the form's submit element and click it
    submit_button = form_element.find_element(by=By.XPATH, value=".//*[@type='submit']")
    submit_button.click()

    return driver
