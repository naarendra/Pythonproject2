from selenium.webdriver.common.by import By
class login_admin_page:
    textbox_username_id = "Email"
    testbox_password_id = "Password"
    testbox_login_xpath ="//button[@type='submit']"
    logout_linktext = "Logout"

    def __init__(self,driver): # accept driver as parameter
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.testbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.testbox_login_xpath).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT,self.logout_linktext).click()



