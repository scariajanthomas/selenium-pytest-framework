import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:

    @pytest.fixture(autouse=True)
    def login(self, driver):
        """Login before every test in this class."""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        self.inventory = InventoryPage(driver)

    def test_inventory_page_loads(self, driver):
        """Inventory page should load after login."""
        assert self.inventory.is_loaded()

    def test_all_six_products_displayed(self, driver):
        """All 6 products should be visible."""
        items = self.inventory.get_all_item_names()
        assert len(items) == 6

    def test_sort_by_price_low_to_high(self, driver):
        """Prices should be in ascending order after sorting."""
        self.inventory.sort_by("lohi")
        prices = self.inventory.get_all_prices()
        assert prices == sorted(prices)

    def test_sort_by_price_high_to_low(self, driver):
        """Prices should be in descending order after sorting."""
        self.inventory.sort_by("hilo")
        prices = self.inventory.get_all_prices()
        assert prices == sorted(prices, reverse=True)

    def test_sort_by_name_a_to_z(self, driver):
        """Product names should be in A-Z order."""
        self.inventory.sort_by("az")
        names = self.inventory.get_all_item_names()
        assert names == sorted(names)

    def test_add_item_to_cart(self, driver):
        """Cart badge should show 1 after adding one item."""
        self.inventory.add_first_item_to_cart()
        assert self.inventory.get_cart_count() == 1