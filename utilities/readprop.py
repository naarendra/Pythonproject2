import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_config:
    @staticmethod
    def get_admin_pageurl():
        url= config.get('admin login information','admin_page_url')
        return url
    @staticmethod
    def get_usrnam():
        uname= config.get('admin login information','username')
        return uname
    @staticmethod
    def get_password():
        pasd= config.get('admin login information','password')
        return pasd
    @staticmethod
    def get_invusername():
        invur= config.get('admin login information','invalidusername')
        return invur