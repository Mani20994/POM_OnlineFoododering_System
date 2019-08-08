class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.Restaurants_button_xpath = "//a[contains(@href,'https://www.demo.iscripts.com/netmenus/mrml/cms?section=restaurant')][contains(text(),'Restaurants')]"
        self.manage_button_xpath = "//tr[@id='jqRecord_23']//td[8]"
        self.addfooditem_button_id = "additem"
        #self.item_button_id = "activities_id"
        self.fooditem_textbox_id = "activities_id"
        self.fooddescription_textbox_name = "activity_description"
        self.menuitem_button_id = "menus"
        self.price_textbox_id = "activity_price"
        self.foodcategory_button_xpath = "//div[@class='controls']//ul[@class='token-input-list-facebook']"
        self.category_textbox_id = "token-input-food_category"
        self.categoryenter_textbox_id = "token-input-food_category"
        self.foodsave_button_name = "submit"

        self.Restaurants_button_xpath = "//a[contains(@href,'https://www.demo.iscripts.com/netmenus/mrml/cms?section=restaurant')][contains(text(),'Restaurants')]"
        self.searchField_button_xpath = "//select[@id='searchField']"
        self.searchText_textbox_id = 'searchText'
        self.search_button_id = "section_search_button"
        self.publish_button_xpath = "//tr[5]//td[10]//a[1]//button[1]"

        self.addrecord_button_xpath = "//a[@class='addrecord btn btn-info']"
        self.restaurant_textbox_id = "venue_name"
        self.description_textbox_id = "venue_description"
        self.address_textbox_id = "venue_address_by_user"
        self.zip_textbox_id = "zip_code"
        self.phone_textbox_id = "phone"
        self.cuisines_textbox_id = "tags"
        self.paymentoption_button_name = "is_payment_direct"
        self.takeout_button_id = "takout"
        self.reservation_button_id = "reservation"
        self.restaurantowner_textbox_id = "created_by"
        self.manager_textbox_id = "store_manager"
        self.manageremail_textbox_id = "store_manager_email"
        self.minimumorder_textbox_id = "min_order_amount"
        self.salestax_textbox_id = "sales_tax"
        self.deliveryfee_textbox_id = "delivery_fee"
        self.rateofcommission_textbox_id = "commission"
        self.save_button_id = "jqSubmitForm"

        self.addcuisines_button_xpath = "//a[contains(text(),'Cuisines')]"
        self.record_button_xpath = "//a[@class='addrecord btn btn-info']"
        self.tag_textbox_id = "tag_name"
        self.cuisinesiamge_button_id = "//input[@id='tag_image']"
        self.savebutton_button_id = "jqSubmitForm"
        self.logout_button_xpath = "//a[@class='icon_logout']"

    def click_restaurant(self):
        self.driver.find_element_by_xpath(self.Restaurants_button_xpath).click()

    def click_manage(self):
        self.driver.find_element_by_xpath(self.manage_button_xpath).click()

    def click_addfooditem(self):
        self.driver.find_element_by_id(self.addfooditem_button_id).click()

    def enter_fooditem(self, itemname):
        self.driver.find_element_by_id(self.fooditem_textbox_id).send_keys(itemname)

    #def enter_item(self, item):
            #self.driver.find_element_by_id(self.fooditem_textbox_id).send_keys(item)

    def enter_fooddescription(self, description):
        self.driver.find_element_by_name(self.fooddescription_textbox_name).send_keys(description)

    def click_menu(self):
        self.driver.find_element_by_id(self.menuitem_button_id).click()

    def enter_price(self, price):
        self.driver.find_element_by_id(self.price_textbox_id).send_keys(price)

    def click_foodcategory(self):
        self.driver.find_element_by_xpath(self.foodcategory_button_xpath).click()

    def enter_category(self, categoryname):
        self.driver.find_element_by_id(self.category_textbox_id).send_keys(categoryname)

    def enter_buttonenter(self, buttonenter):
        self.driver.find_element_by_id(self.categoryenter_textbox_id).send_keys(buttonenter)

    def click_clicksave(self):
        self.driver.find_element_by_name(self.foodsave_button_name).click()

    def click_restaurants(self):
        self.driver.find_element_by_xpath(self.Restaurants_button_xpath).click()

    def click_searchfield(self):
        self.driver.find_element_by_xpath(self.searchField_button_xpath).click()

    def enter_searchtext(self, searchtext):
        self.driver.find_element_by_id(self.searchText_textbox_id).send_keys(searchtext)

    def click_searchbutton(self):
        self.driver.find_element_by_id(self.search_button_id).click()

    def click_publish(self):
            self.driver.find_element_by_xpath(self.publish_button_xpath).click()

    def click_addrecord(self):
        self.driver.find_element_by_xpath(self.addrecord_button_xpath).click()

    def enter_restaurants(self, restaurant):
        self.driver.find_element_by_id(self.restaurant_textbox_id).send_keys(restaurant)

    def enter_description(self, description):
        self.driver.find_element_by_id(self. description_textbox_id).send_keys(description)

    def enter_address(self, address):
        self.driver.find_element_by_id(self.address_textbox_id ).send_keys(address)

    def enter_zip(self, zip):
        self.driver.find_element_by_id(self.zip_textbox_id).send_keys(zip)

    def enter_phone(self, phone):
        self.driver.find_element_by_id(self.phone_textbox_id).send_keys(phone)

    def enter_cuisines(self, cuisines):
        self.driver.find_element_by_id(self.cuisines_textbox_id).send_keys(cuisines)

    def click_payment(self):
        self.driver.find_element_by_name(self.paymentoption_button_name).click()

    def click_takeout(self):
        self.driver.find_element_by_id(self.takeout_button_id).click()

    def click_reservation(self):
        self.driver.find_element_by_id(self.reservation_button_id).click()

    def enter_owner(self, owner):
        self.driver.find_element_by_id(self.restaurantowner_textbox_id).send_keys(owner)

    def enter_manager(self, manager):
        self.driver.find_element_by_id(self.manager_textbox_id).send_keys(manager)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.manageremail_textbox_id).send_keys(email)

    def enter_order(self, order):
        self.driver.find_element_by_id(self.minimumorder_textbox_id).send_keys(order)

    def enter_salestax(self, salestax):
        self.driver.find_element_by_id(self.salestax_textbox_id).send_keys(salestax)

    def enter_fee(self, fee):
        self.driver.find_element_by_id(self.deliveryfee_textbox_id).send_keys(fee)

    def enter_commission(self, commission):
        self.driver.find_element_by_id(self.rateofcommission_textbox_id).send_keys(commission)

    def click_saves(self):
        self.driver.find_element_by_id(self.save_button_id).click()

    def click_addcuisines(self):
        self.driver.find_element_by_xapth(self.addcuisines_button_xpath).click()

    def click_record(self):
        self.driver.find_element_by_xpath(self.record_button_xpath).click()

    def enter_tag(self, tag):
        self.driver.find_element_by_id(self.tag_textbox_id).send_keys(tag)

    def enter_image(self, image):
        self.driver.find_element_by_id(self.cuisinesiamge_button_id).send_keys(image)

    def click_savebutton(self):
        self.driver.find_element_by_id(self.cuisinesiamge_button_id).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()

