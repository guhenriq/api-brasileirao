from selenium import webdriver


class Browser:

    def __init__(self) -> None:
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless=new')
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def close(self):
        if self:
            self.driver.quit()

