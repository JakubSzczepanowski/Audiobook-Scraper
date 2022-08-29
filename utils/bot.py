from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class ChromeBot:
    
    def __init__(self, driver_path: str):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(driver_path, options=option)

    def get_video_src(self, url: str) -> str:
        self.driver.get(url)

        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "video"))).get_attribute("src")
    
    def close(self):
        self.driver.close()




