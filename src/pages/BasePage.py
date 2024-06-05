from src.util.getEnv import get_env


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.defaultUrl = get_env("defaultUrl")

    def page_move(self, url):
        self.driver.get(url)

    def run_test(self):
        """
        여기서 테스트 스크립트를 작성해 주세요
        """
