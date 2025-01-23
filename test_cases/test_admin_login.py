import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages import loginadminpage
from base_pages.loginadminpage import login_admin_page
from utilities.readprop import Read_config
from utilities.custom_logger import log_Maker
class Test_01_admin_login:

    admin_page_url= Read_config.get_admin_pageurl()
    username = Read_config.get_usrnam()
    password=Read_config.get_password()
    invalidusername =Read_config.get_invusername()
    logger= log_Maker.log_gen()
    @pytest.mark.regression
    def title_verification(self):
        self.logger.info("***********title verification started****************")
        self.driver= webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        act_title=self.driver.title
        expect_title="nopCommerce demo store. Login"
        if act_title==expect_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
    @pytest.mark.sanity
    def test_validadmin_login(self):
        self.logger.info("***********Testing validadmin login case****************")
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.admin_log= login_admin_page(self.driver)
        self.admin_log.enter_username(self.username)
        self.admin_log.enter_password(self.password)
        self.admin_log.click_login()
