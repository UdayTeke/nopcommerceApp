

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.Loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):

        self.logger.info("***********  Test_001_Login  ***********")
        self.logger.info("***********  Verifying Home page Title  ***********")
        self.driver = setup
        self.driver.get(self.baseURL)

        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********** Home page title test is passed  ***********")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitle.png")
            assert False
            self.driver.close()
            self.logger.error("*********** Home page title test is Failed ***********")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.logger.info("*********** verifying Login test  ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*********** Login page title test is passed  ***********")


        else:
            self.driver.save_screenshot(".//ScreenShots" + "test_Login.png")
            assert False
            self.driver.close()
            self.logger.error("*********** Login page title test is Failed ***********")
