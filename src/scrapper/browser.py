from selenium import webdriver


class Browser:

    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome()

    def close(self):
        if self:
            self.driver.quit()

