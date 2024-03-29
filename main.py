from selenium import webdriver
from selenium.webdriver.common.by import By
from db import MongoDriver

driver = webdriver.Chrome()
driver.get("https://ecuador.patiotuerca.com/")
search_box = driver.find_element(by=By.CSS_SELECTOR, value="#search-list")
search_box.send_keys("Audi A4")

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#openSearch > div > div > div.search-ots.false > img")
search_button.click()

vehicle_cards = driver.find_elements(By.CSS_SELECTOR, "#featuredUsed > div.xl3")

mongodbC = MongoDriver()

for card in vehicle_cards:
    try:
        title = card.find_element(By.CSS_SELECTOR, "div > div > div > div.card-info.card-content > div.module.tittle").text
        kms_y_city = card.find_element(By.CSS_SELECTOR, "div > div > div > div.card-info.card-content > div.latam-secondary-text.text-lighten-2.left.vehicle-highlight").text
        price = card.find_element(By.CSS_SELECTOR, "div > div > div > div.card-info.card-content > strong").text
        print(title)
        print(kms_y_city)
        print(f"${price}")

        nwAuto = {
            "title": title,
            "kms_y_city": kms_y_city,
            "price": price
        }
        mongodbC.insert_record(record=nwAuto,username="auto")
        print("--------------------------------")
    except Exception as e:
        print(e)
        print("++++++++++++++++++++++++++++++++")


driver.close()
