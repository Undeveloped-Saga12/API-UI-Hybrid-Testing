import pytest
from pages.login_page import LoginPage
from utils.api_client import APIClient

def test_hybrid_api_ui_login(browser):
    # Step 1: Create a user using the API
    api=APIClient()
    user_data=api.create_user(name="Sagar",job="Automation Engineer")
    print(f"API Response:{user_data}")

    #Step 2: UI-log in with the same credentials
    login_page=LoginPage(browser)
    login_page.open()
    login_page.login("standard_user","secret_sauce")

    assert login_page.is_dashboard_displayed(),"UI login failed"