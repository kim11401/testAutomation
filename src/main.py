import concurrent.futures

from selenium import webdriver

from pages.loginPage.test.login_test import LoginTest


def run_test(browser_name):
    if browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    try:
        LoginTest.run_test(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    browsers = ["firefox", "chrome", "safari"]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_test, browser) for browser in browsers]

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Test failed: {e}")
