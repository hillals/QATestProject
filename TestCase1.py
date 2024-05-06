import time
import unittest
from selenium import webdriver
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
        element = driver.find_element(By.ID, QAPage.accept_button)
        element.click()
        # See all QA jobs button
        element = driver.find_element(By.XPATH, QAPage.allQA_button)
        element.click()
        #  All jobs dropdown
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, QAPage.QA_dropdown)))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, QAPage.Loc_dropdown)))
        drop = driver.find_element(By.XPATH, QAPage.Loc_dropdown)
        drop.click()
        time.sleep(2)
        #  Select Istanbul, Turkey
        option = driver.find_element(By.XPATH, QAPage.Ist_dropdown)
        option.click()
        #  Check locations and departments
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, QAPage.position_QualityAssurance)))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, QAPage.position_QA)))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, QAPage.QA_dropdown)))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, QAPage.location_Ist)))
        action = ActionChains(driver)
        #  Move to QA manager to access View Role button
        position = driver.find_element(By.XPATH, QAPage.position_QAManager)
        action.move_to_element(position).click().perform()
        button = driver.find_element(By.XPATH, QAPage.btn_ViewRole)
        button.click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_changes(QAPage.role_url))

    def tearDown(self):
        self.driver.save_screenshot('screenshots/screenshotTest1.png')
        self.driver.close()


# execute the script
if __name__ == "__main__":
    unittest.main()

