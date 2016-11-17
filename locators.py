from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_FIRST = (By.XPATH, "//input[@id='index_email']")
    PASS_FIRST = (By.XPATH, "//input[@id='index_pass']")
    FOREIGN_COMP_FIRST = (By.XPATH, "//div[@id='index_expire']")
    GO_BUTTON_FIRST = (By.XPATH, "//button[@id='index_login_button']")
    OPTION_FIRST = (By.XPATH, "//div/a[@id='top_profile_link']")
    OUT_FIRST = (By.XPATH, "//div/a[@id='top_logout_link']")

    LOGIN_AFTER_OUT = (By.XPATH, "//input[@id='quick_email']")
    PASS_AFTER_OUT = (By.XPATH, "//input[@id='quick_pass']")
    FOREIGN_COMP_AFTER_OUT = (By.XPATH, "//div[@id='quick_expire']")
    GO_BUTTON_AFTER_OUT = (By.XPATH, "//button[@id='quick_login_button']") 

    LOGIN_AFTER_INCORRECT = (By.XPATH, "//input[@id='email']")
    PASS_AFTER_INCORRECT = (By.XPATH, "//input[@id='pass']")
    GO_BUTTON_AFTER_INCORRECT = (By.XPATH, "//button[@id='login_button']")

