import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Login before every test."""
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        self.inventory = InventoryPage(driver)
        self.cart = CartPage(driver)

    def test_cart_empty_by_default(self, driver):
        """Cart should be empty before adding any item."""
        self.inventory.go_to_cart()
        assert self.cart.is_cart_empty()

    def test_add_one_item_to_cart(self, driver):
        """Cart should contain one item after adding."""
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()
        assert self.cart.get_cart_item_count() == 1

    def test_remove_item_from_cart(self, driver):
        """Cart should be empty after removing the only item."""
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()
        self.cart.remove_first_item()
        assert self.cart.is_cart_empty()

    def test_continue_shopping_navigates_back(self, driver):
        """Continue shopping should return to inventory page."""
        self.inventory.go_to_cart()
        self.cart.continue_shopping()
        assert "/inventory" in driver.current_url

    def test_checkout_button_navigates_to_checkout(self, driver):
        """Checkout button should navigate to checkout page."""
        self.inventory.add_first_item_to_cart()
        self.inventory.go_to_cart()
        self.cart.proceed_to_checkout()
        assert "/checkout-step-one" in driver.current_url