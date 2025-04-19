import pytest
from selenium import webdriver
from .login_page2 import LoginPage2
from .admin_page_2 import AdminPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_verify_user_exists(driver):
    login = LoginPage2(driver)
    admin = AdminPage(driver)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin", "admin123")

    admin.open_admin_tab()
    admin.search_user("peter2346")

    assert admin.is_user_listed("peter2346"), "User 'peter2345' not found."
