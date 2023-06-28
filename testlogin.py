from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import unittest


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-notifications')


class webtest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options = options)

    def test_login(self):
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME,'username').send_keys('Admin')
        self.driver.find_element(By.NAME,'password').send_keys('admin123' + Keys.RETURN)
        time.sleep(3)
        assert 'OrangeHRM' in self.driver.title
        

    def test_login_FAILED_WrongPassword(self):
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME,'username').send_keys('Admin')
        self.driver.find_element(By.NAME,'password').send_keys('admin356' + Keys.RETURN)
        time.sleep(3)
        invalid = self.driver.find_element(By.ID,'app').text
        self.assertIn('Invalid credentials', invalid)
    


    def test_logout(self):
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME,'username').send_keys('Admin')
        self.driver.find_element(By.NAME,'password').send_keys('admin123' + Keys.RETURN)
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME,"oxd-userdropdown").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()
        time.sleep(5)    
        login_button = self.driver.find_element(By.XPATH,'//button[@type="submit"]').text
        self.assertIn('Login', login_button)


    def test_Menu_Admin(self):
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME,'username').send_keys('Admin')
        self.driver.find_element(By.NAME,'password').send_keys('admin123' + Keys.RETURN)
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//a[@href="/web/index.php/admin/viewAdminModule"]').click()
        time.sleep(3)
        management = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6[2]').text
        self.assertIn('User Management', management)
    

    def tearDown(self):
        self.driver.quit()

    

if __name__ == '__main__':
    unittest.main()