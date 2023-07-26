from fake_useragent import UserAgent
from dataclasses import dataclass
from requests_html import HTML

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


def get_user_agent():
    return UserAgent(verify_ssl=False).random



@dataclass
class Scraper:
    url: str
    driver: WebDriver = None
    html_obj: HTML = None

    def get_driver(self):
        if self.driver == None:
            user_agent = get_user_agent()
            options = Options()
            options.add_argument("--no-sandbox")
            # options.add_argument("--headless")
            options.add_argument(f"user-agent={user_agent}")
            driver = webdriver.Chrome(options=options)

            self.driver = driver
        return self.driver

   
    def get(self):
        driver = self.get_driver()
        driver.get(self.url)

        return driver.page_source