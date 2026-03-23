import pytest
from pages.login_page import LoginPage


class TestLogin:

    def test_valid_login(self, driver):
        """Valid credentials should land on inventory page."""
        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        assert "/inventory" in driver.current_url

    def test_invalid_password(self, driver):
        """Wrong password should show error message."""
        login = LoginPage(driver)
        login.login("standard_user", "wrong_password")

        error = login.get_error_message()
        assert "Username and password do not match" in error

    def test_empty_username(self, driver):
        """Empty username should show error message."""
        login = LoginPage(driver)
        login.open()
        login.click_login()

        error = login.get_error_message()
        assert "Username is required" in error

    def test_locked_out_user(self, driver):
        """Locked out user should see specific error."""
        login = LoginPage(driver)
        login.login("locked_out_user", "secret_sauce")

        error = login.get_error_message()
        assert "locked out" in error.lower()