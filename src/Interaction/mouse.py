from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Mouse:
    def __init__(self, driver):
        """
        Initialize the Mouse class with a WebDriver instance.

        :param driver: WebDriver, The WebDriver instance to be used.
        """
        self.driver = driver

    def left_click(self, locator, timeout=10):
        """
        Perform a left click on the element located by the given locator.

        :param locator: tuple, The locator for the element to be clicked.
        :param timeout: int, The maximum amount of time to wait for the element to be clickable.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except Exception as e:
            print(f"Exception occurred while trying to left click on the element: {e}")

    def right_click(self, locator, timeout=10):
        """
        Perform a right click on the element located by the given locator.

        :param locator: tuple, The locator for the element to be clicked.
        :param timeout: int, The maximum amount of time to wait for the element to be clickable.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            ActionChains(self.driver).context_click(element).perform()
        except Exception as e:
            print(f"Exception occurred while trying to right click on the element: {e}")

    def left_double_click(self, locator, timeout=10):
        """
        Perform a left double click on the element located by the given locator.

        :param locator: tuple, The locator for the element to be double clicked.
        :param timeout: int, The maximum amount of time to wait for the element to be clickable.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            ActionChains(self.driver).double_click(element).perform()
        except Exception as e:
            print(
                f"Exception occurred while trying to left double click on the element: {e}"
            )

    def right_double_click(self, locator, timeout=10):
        """
        Perform a right double click on the element located by the given locator.

        :param locator: tuple, The locator for the element to be double clicked.
        :param timeout: int, The maximum amount of time to wait for the element to be clickable.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            ActionChains(self.driver).context_click(element).perform()
            ActionChains(self.driver).context_click(
                element
            ).perform()  # Simulate double right click
        except Exception as e:
            print(
                f"Exception occurred while trying to right double click on the element: {e}"
            )

    def scroll_down(self, pixels=100):
        """
        Scroll down by a specified number of pixels.

        :param pixels: int, The number of pixels to scroll down.
        """
        try:
            self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        except Exception as e:
            print(f"Exception occurred while trying to scroll down: {e}")

    def scroll_up(self, pixels=100):
        """
        Scroll up by a specified number of pixels.

        :param pixels: int, The number of pixels to scroll up.
        """
        try:
            self.driver.execute_script(f"window.scrollBy(0, -{pixels});")
        except Exception as e:
            print(f"Exception occurred while trying to scroll up: {e}")
