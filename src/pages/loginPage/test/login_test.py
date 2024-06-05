from src.pages.BasePage import BasePage
from src.pages.loginPage.locators import LoginPageLocators as locators


class LoginTest(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = self.defaultUrl + locators.URL

    def run_test(self):
        self.page_move(self.url)
