from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from com.qa.POMProject.POMFiles.Pages.loginpage import LoginPage
from com.qa.POMProject.POMFiles.Pages.homePage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\Nxt\\PycharmProjects\\POM(Online Food odering)\\Drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.demo.iscripts.com/netmenus/mrml/cms")

        login = LoginPage(driver)
        login.enter_username("admin")
        login.enter_password("admin")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_restaurant()
        homepage.click_manage()
        homepage.click_addfooditem()
        homepage.enter_fooditem("Gobhi Aloo")
        #homepage.enter_item("keys.ENTER")
        homepage.enter_fooddescription("Starter")
        homepage.click_menu()
        homepage.enter_price("250")
        time.sleep(2)
        homepage.click_foodcategory()
        time.sleep(2)
        homepage.enter_category("Pizza")
        time.sleep(2)
        homepage.enter_buttonenter(Keys.ENTER)
        time.sleep(2)
        homepage.click_clicksave()

        homepage.click_restaurants()
        homepage.click_searchfield()
        homepage.enter_searchtext("paradise")
        time.sleep(2)
        homepage.click_searchbutton()
        homepage.click_publish()
        homepage.click_addrecord()
        time.sleep(2)
        homepage.enter_restaurants("Paradise")
        homepage.enter_description("Good restaurant")
        homepage.enter_address("Hyderabad")
        homepage.enter_zip("123456")
        time.sleep(2)
        homepage.enter_phone("98765543234")
        homepage.enter_cuisines("Cakes-Bakery")
        homepage.click_payment()
        homepage.click_takeout()
        homepage.click_reservation()
        time.sleep(2)
        homepage.enter_owner("William Brown")
        homepage.enter_manager("Robert")
        homepage.enter_email("robert@gamil.com")
        homepage.enter_order("5000")
        time.sleep(2)
        homepage.enter_salestax("10")
        homepage.enter_fee("15")
        time.sleep(2)
        homepage.enter_commission("20")
        homepage.click_saves()
        time.sleep(2)

        homepage.click_addcuisines()
        time.sleep(2)
        homepage.click_record()
        time.sleep(2)
        homepage.enter_tag("French drinks")
        homepage.enter_image("C:\\Users\\Nxt\\Pictures\\Restaurant.jpg")
        time.sleep(2)
        homepage.click_savebutton()

        homepage.click_logout()

        #self.driver.get("https://www.demo.iscripts.com/netmenus/mrml/cms")
        #self.driver.find_element_by_id("username").send_keys("admin")
        #self.driver.find_element_by_id("inputPassword").send_keys("admin")
        #self.driver.find_element_by_name("submit").click()
        #time.sleep(2)
        #self.driver.find_element_by_xpath("//a[contains(@href,'https://www.demo.iscripts.com/netmenus/mrml/cms?section=restaurant')][contains(text(),'Restaurants')]").click()
        #self.driver.find_element_by_xpath("//select[@id='searchField']").click()
        #self.driver.find_element_by_id("searchText").send_keys("paradise")
        #self.driver.find_element_by_id("section_search_button").click()
        #self.driver.find_element_by_xpath("//tr[5]//td[10]//a[1]//button[1]").click()
        #self.driver.find_element_by_xpath("//a[@class='icon_logout']").click()
        #time.sleep(2)

    # @classmethod
    # def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        # print("Test Completed")


if __name__ == '__main__':
    unittest.main()

