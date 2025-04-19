import pytest
from selenium import webdriver
from.login_page2 import LoginPage2
from .dashboard_page_2 import DashboardPage2
from.admin_page_2 import AdminPage

ADMIN_USERNAME = "Admin"
ADMIN_PASSWORD = "admin123"
EMPLOYEE_NAME = "Peter Mac Anderson"
NEW_USERNAME = "peter2345"
NEW_PASSWORD = "Test234"
URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()

def test_create_user_flow(browser):
    login = LoginPage2(browser)
    dashboard = DashboardPage2(browser)
    admin = AdminPage(browser)

    login.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    assert dashboard.is_dashboard_displayed()

    admin.open_admin_tab()
    admin.add_user(EMPLOYEE_NAME, NEW_USERNAME, NEW_PASSWORD)
    assert admin.verify_success()

    dashboard.logout()
    login.login(NEW_USERNAME, NEW_PASSWORD)
    assert dashboard.is_dashboard_displayed()
