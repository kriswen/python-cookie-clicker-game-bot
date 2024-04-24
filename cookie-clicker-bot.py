from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# cookie
cookie = driver.find_element(By.ID, value="cookie")

# set timer for 5 min
timeout_5m = time.time() + 60 * 5  # 5 min from now
timeout_5s = time.time() + 5  # 5 sec from now

# get all items
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items[0:-1]]

print(f"time start: {time.time()}")
while True:
    # click all time
    cookie.click()
    # end the program after 5m
    if time.time() > timeout_5m:
        cookie_per_sec = driver.find_element(By.ID, value="cps").text
        print(f"Cookies/second: {cookie_per_sec}")
        print(f"time ended: {time.time()}")
        driver.quit()
        break
    # only run the following every 5 sec
    if time.time() > timeout_5s:
        # get all new prices for the items (b tags within id of store)
        all_items_with_prices = {}
        all_upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        for i in range(len(all_upgrades)-1):
            # create dict of items and its prices
            item_id = item_ids[i]

            item_cost = int(all_upgrades[i].text.split()[-1].replace(",", ""))
            # add to dict
            all_items_with_prices[item_id] = item_cost
        # print(all_items_with_prices)
        # get current money/cookie
        money_string = driver.find_element(By.ID, value="money").text
        if "," in money_string:
            money_string = money_string.replace(",", "")
        money = int(money_string)
        print(f"Current money: ${money}")
        # find all upgrade items that we can afford currently
        affordable_items = {}
        for item_id, cost in all_items_with_prices.items():
            if money >= cost:
                affordable_items[cost] = item_id
        print(f"Current affordable upgrades are: {affordable_items}")
        # find and purchase most expensive upgrade item
        most_exp_upgrade = max(affordable_items)
        to_purchase_item = affordable_items[most_exp_upgrade]
        # click on most exp item that is affordable to purchase
        driver.find_element(By.ID, value=to_purchase_item).click()
        print(f"Most expensive upgrade {to_purchase_item} was purchased.")
        # add another 5 sec for next check
        timeout_5s = time.time() + 5

