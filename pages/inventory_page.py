from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    # Locators
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        """Confirm inventory page is loaded."""
        self.wait.until(EC.visibility_of_element_located(self.INVENTORY_CONTAINER))
        return "/inventory" in self.driver.current_url

    def get_all_item_names(self):
        """Return list of all product names."""
        items = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_NAMES))
        return [item.text for item in items]

    def get_all_prices(self):
        """Return list of all prices as floats."""
        prices = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_PRICES))
        return [float(p.text.replace("$", "")) for p in prices]

    def sort_by(self, option):
        """Sort products. Options: 'az', 'za', 'lohi', 'hilo'."""
        dropdown = self.wait.until(EC.visibility_of_element_located(self.SORT_DROPDOWN))
        Select(dropdown).select_by_value(option)

    def add_first_item_to_cart(self):
        """Add first available item to cart."""
        buttons = self.wait.until(EC.presence_of_all_elements_located(self.ADD_TO_CART_BUTTONS))
        buttons[0].click()

    def get_cart_count(self):
        """Return cart badge count as int."""
        badge = self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))
        return int(badge.text)

    def go_to_cart(self):
        """Click cart icon to navigate to cart."""
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()

    def go_to_cart(self):
        """Click cart icon — stays in same session, preserves cart state."""
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()
        self.wait.until(EC.url_contains("cart"))