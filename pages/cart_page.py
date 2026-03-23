from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    URL = "https://www.saucedemo.com/cart.html"

    # Locators
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "[data-test^='remove']")
    CONTINUE_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        return self.driver.current_url == self.URL

    def get_cart_items(self):
        try:
            items = self.driver.find_elements(*self.ITEM_NAME)
            return [i.text for i in items]
        except:
            return []

    def get_cart_item_count(self):
        return len(self.get_cart_items())

    def remove_first_item(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.REMOVE_BUTTON))
        btn.click()

    def is_cart_empty(self):
        return self.get_cart_item_count() == 0

    def continue_shopping(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def proceed_to_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()