from selenium import webdriver
import chromedriver_autoinstaller
from PageObject.testPageFile import LoginPage


def test_Login():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("https://s1.demo.opensourcecms.com/wordpress/wp-login.php")

    pglogin = LoginPage(driver)
    # method calling example
    # pglogin.login()
    pglogin.edtUserName.set_text("opensourcecms")  # edtUserName become class variable using PageFactory
    pglogin.edtPassword.set_text("opensourcecms")
    pglogin.btnSignIn.click_button()
