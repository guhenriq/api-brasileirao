from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Browser:

    def __init__(self) -> None:
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless=new')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)

    def close(self):
        if self:
            self.driver.quit()

