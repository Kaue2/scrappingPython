from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class htmlpage:
    def __init__(self, url) -> None:
        self.url = url
        self.driver = ''
        self.htmlContent = ''
        self.getDriver(url)
        self.saveHtml()

    def getDriver(self, url) -> None:
        # usar try catch
        self.driver = webdriver.Firefox()
        self.driver.get(url)

        WebDriverWait(self.driver, 120).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        
        self.htmlContent = self.driver.page_source
        

    def saveHtml(self) -> None:
        with open("htmlDoSelenium.html", "w", encoding="utf-8") as file:
            file.write(self.htmlContent)