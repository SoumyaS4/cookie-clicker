import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = "C:\selenium\chromedriver.exe"
service_obj= Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome()

# driver.get("https://www.amazon.com/Ovente-KG83B-BPA-Free-Protection-Indicator/dp/B00DEPGY7G/ref=sr_1_2_sspa?crid=1Q8HNX37C5T7P&keywords=kettle&qid=1683468363&sprefix=kett%2Caps%2C350&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFZRUdQTTZWRFNKVFEmZW5jcnlwdGVkSWQ9QTA3NTE3MTQyR0Y2Tzg0TzdVSFlDJmVuY3J5cHRlZEFkSWQ9QTA1MTY5MjMxR0JQODRENkNaNzVFJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
# price = driver.find_elements(By.CLASS_NAME,"a-offscreen")
# lists=[]
#     prices = ele.get_attribute("innerHTML")
#     lists.append(prices)
# print(lists[0])
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

# I think timeout should be set bigger to inscrease the possibility for buying more expensive tool
timeout = time.time() + 10
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:
        # get current money
        money = driver.find_element(By.ID, "money").text
        if "," in money:
            current_money = int(money.replace(",", ""))
        else:
            current_money = int(money)

        # buy tool
        store = driver.find_elements(By.CSS_SELECTOR, "#store b")
        for upgrade in store[::-1]:
            upgrade_text = upgrade.text
            if upgrade_text != "":
                detail = upgrade_text.split("-")
                product = detail[0].strip()
                cost = detail[-1].strip()
                if "," in cost:
                    cost = cost.replace(",", "")
                cost_int = int(cost)
                if current_money >= cost_int:
                    driver.find_element(By.ID, f"buy{product}").click()
                    break
                else:
                    continue

        timeout = time.time() + 10

    if time.time() > five_min:
        cookie_per = driver.find_element(By.ID, "cps").text
        print(cookie_per)
        break



driver.quit()