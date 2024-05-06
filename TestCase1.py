import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.qa_page import QAPage


class TestCase1(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Test case method. It should always start with test_
    def test_search_qa_jobs(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(QAPage.qa_url)
        #  Accept all button
        element = driver.find_element(By.ID, 'wt-cli-accept-all-btn')
        element.click()
        # See all QA jobs button
        element = driver.find_element(By.XPATH, '/html/body/div[1]/section[1]/div/div/div/div[1]/div/section/div/div/div[1]/div/div/a')
        element.click()
        #  All jobs dropdown
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[contains (text(),'Quality Assurance')]")))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[contains (text(),'All')]")))
        drop = driver.find_element(By.XPATH, "//span[contains (text(),'All')]")
        drop.click()
        time.sleep(2)
        #  Select Istanbul, Turkey
        option = driver.find_element(By.XPATH, "//li[contains (text(),'Istanbul, Turkey')]")
        option.click()
        #  Check locations and departments
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//p[contains (text(),'Quality Assurance')]")))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//p[contains (text(),'QA')]")))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[contains (text(),'Quality Assurance')]")))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[contains (text(),'Istanbul, Turkey')]")))
        action = ActionChains(driver)
        position = driver.find_element(By.XPATH, '//*[@id="jobs-list"]/div[4]/div')
        action.move_to_element(position).click().perform()
        button = driver.find_element(By.XPATH, "/html/body/section[3]/div/div/div[2]/div[4]/div/a")
        button.click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_changes('https://jobs.lever.co/useinsider/285ebdc7-e10b-416d-a636-bab5ec81d852'))


    def tearDown(self):
        self.driver.close()


# execute the script
if __name__ == "__main__":
    unittest.main()

