from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as WdW
import time as t


class SeleniumDriver:
    def __init__(self):
        url = 'https://orteil.dashnet.org/cookieclicker/'
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = Chrome(options=options)
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def lng_selection(self):
        try:
            selection_box = WdW(self.driver, 10).until(
                ec.presence_of_element_located((By.XPATH, '//*[@id="langSelect-EN"]'))
            )

        except Exception as exc:
            print("Selection operation skipped.", exc)

        else:
            selection_box.click()

        finally:
            self.driver.implicitly_wait(5)

    def click_method(self):
        text = ''
        t.sleep(5)
        try:
            text = "cookie cursor"
            cookie_cursor = self.driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

            text = "upgrade 1 button"
            upgrade_1 = self.driver.find_element(By.XPATH, '//*[@id="product0"]')

            text = "upgrade 2 button"
            upgrade_2 = self.driver.find_element(By.XPATH, '//*[@id="product1"]')

        except Exception as exc:
            print("!!! Error while locating " + text + ' !!!\n', exc)

        else:
            self.driver.implicitly_wait(5)
            count_upgrade_1 = 0
            count_upgrade_2 = 0
            surplus_storage = 20

            for i in range(1, 2001):
                if i % 500 == 1:
                    print("• Progress: ", (i/2000)*100, '%')

                cookie_cursor.click()

                try:
                    text = "cookie counter"
                    cookie_counter = self.driver.find_element(By.XPATH, '//*[@id="cookies"]')
                    cookie_value = int(cookie_counter.text.split(' ')[0])

                    text = "upgrade 1 cost"
                    cost_upgrade_1 = self.driver.find_element(By.XPATH, '//*[@id="productPrice0"]')
                    value_upgrade_1 = int(cost_upgrade_1.text)

                    text = "upgrade 2 cost"
                    cost_upgrade_2 = self.driver.find_element(By.XPATH, '//*[@id="productPrice1"]')
                    value_upgrade_2 = int(cost_upgrade_2.text)

                except Exception as exc:
                    print('!!! Failed to locate ' + text + ' !!!\n', exc)

                else:
                    if cookie_value > value_upgrade_1 + surplus_storage:
                        if count_upgrade_1 <= 25:
                            count_upgrade_1 += 1
                            upgrade_1.click()
                            print("◘ Upgrade 1 purchased ", count_upgrade_1, " times\n")

                    elif cookie_value > value_upgrade_2 + surplus_storage:
                        count_upgrade_2 += 1
                        upgrade_2.click()
                        print("◘ Upgrade 2 purchased ", count_upgrade_2, " times\n")



if __name__ == "__main__":
    drv = SeleniumDriver()
    drv.lng_selection()
    drv.click_method()

