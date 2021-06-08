import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    lnkCustomers_menu_xpath=" //i[@class='nav-icon far fa-user']"
    lnkCustomers_menuitem_xpath="//nav/ul/li[4]/ul/li[1]/a/p"
    btnAddNew_xpath="//a[@class='btn btn-primary']"


    txtEmail_xpath="//input[@id='Email' and @name='Email']"
    txtPassword_xpath="//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName' and @name='FirstName']"
    txtLastName_xpath = "//input[@id='LastName' and @name='LastName']"
    rdMaleGender_id = "Gender_Male"
    reFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"

    txtCustomerRoles_xpath="//div[@class='k-multiselect-wrap k-floatwrap' and @role='listbox']"
    lstitemAdministrator_xpath="//li[contains(text(),'Administrator')]"
    lstitemForemModerators_xpath="//li[contains(text(),'Forum Moderators')]"
    lstitemRegistered_xpath="//li[contains(text(),'Registered')]"
    lstitemGuest_xpath="//li[contains(text(),'Guest')]"
    lstitemVendors_xpath="//li[contains(text(),'Vendors')]"
    drpmgrofVendor_xpath="//*[@id='VendorId']"



    txtAdminContain_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"


    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)


    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(4)
        if role == 'Registered':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrator':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemAdministrator_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem=self.driver.find_element_by_xpath(self.lstitemGuest_xpath)
        elif role == 'Foram Moderator':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemForemModerators_xpath)
        elif role == 'Vendors':
            self.listitem=self.driver.find_element_by_xpath(self.lstitemVendors_xpath)

        else:
            self.listitem=self.driver.find_element_by_xpath(self.lstitemGuest_xpath)

        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.drpmgrofVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.reFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContain_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
