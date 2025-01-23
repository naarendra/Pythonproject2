import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages import loginadminpage
from base_pages.loginadminpage import login_admin_page
from utilities.readprop import Read_config
from utilities.custom_logger import log_Maker
from utilities import xl_utilfile

class Test_02_admin_login_data_driven:

    admin_page_url= Read_config.get_admin_pageurl()
    logger= log_Maker.log_gen()
    path=".//test_data//admin_login_data.xlsx"
    status_list=[]


    def test_validadmin_login_datadriven(self):
        self.logger.info("***********Testing validadmin_datadriven login case****************")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://admin-demo.nopcommerce.com/")
        self.admin_log= login_admin_page(self.driver)

        self.rows=xl_utilfile.get_row_count(self.path,"Sheet1")
        print("no.of rows",self.rows)

        for r in range(2,self.rows+1):
            self.username= xl_utilfile.read_data(self.path,"Sheet1",r,1)
            self.password = xl_utilfile.read_data(self.path, "Sheet1", r, 2)
            self.exp_login= xl_utilfile.read_data(self.path, "Sheet1", r, 3)
            self.admin_log.enter_username(self.username)
            self.admin_log.enter_password(self.password)
            self.admin_log.click_login()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp_login== "Yes":
                    self.logger.info("test data is passed")
                    self.status_list.append("Pass")
                    self.admin_log.logout_linktext()
                elif self.exp_login=="No":
                    self.logger.info("test data is failed")
                    self.status_list.append("Fail")
                    self.admin_log.logout_linktext()
            elif act_title != exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data is failed")
                    self.status_list.append("Fail")
                elif self.exp_login == "No":
                     self.status_list.append("Pass")

        print("Status list is",self.status_list)
        if "Fail" in self.status_list:
            self.logger.info(" admin login data driven test case is fail")
            assert False
        else:
            self.logger.info(" data driven test case is pass")
            assert True










