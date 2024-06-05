from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Input:
    def __init__(self, driver):
        """
        Initialize the Keyboard class with a WebDriver instance.

        :param driver: WebDriver, The WebDriver instance to be used.
        """
        self.driver = driver

    def text(self, locator, text, timeout=10):
        """
        Enter text into the element located by the given locator.

        :param locator: tuple, The locator for the element to receive text.
        :param text: str, The text to enter.
        :param timeout: int, The maximum amount of time to wait for the element to be visible.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.send_keys(text)
        except Exception as e:
            print(f"Exception occurred while trying to enter text: {e}")

    def enter(self, locator, timeout=10):
        """
        Press the Enter key on the element located by the given locator.

        :param locator: tuple, The locator for the element.
        :param timeout: int, The maximum amount of time to wait for the element to be visible.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Exception occurred while trying to press Enter: {e}")
