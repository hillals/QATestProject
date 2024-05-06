import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.home_page import HomePage

class TestCase1(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Test case method. It should always start with test_
    def test_search_careers(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(HomePage.url)
        driver.find_element(By.ID, HomePage.confirmHomePage)
        element = driver.find_element(By.LINK_TEXT, HomePage.companyMenu)
        element.click()
        element = driver.find_element(By.XPATH, HomePage.careersDropdown)
        element.click()
        action = ActionChains(driver)
        text = driver.find_element(By.LINK_TEXT, HomePage.textAllTeams)
        action.move_to_element(text).click().perform()
        text = driver.find_element(By.XPATH, HomePage.textOurLocations)
        action.move_to_element(text).click().perform()
        text = driver.find_element(By.XPATH, HomePage.textLifeAtInsider)
        action.move_to_element(text).click().perform()


    def tearDown(self):
        self.driver.save_screenshot('screenshots/screenshotTest2.png')
        self.driver.close()


if __name__ == "__main__":
    unittest.main()