# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from locators import MainPageLocators

class VkComLogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C://chromedriver/chromedriver.exe") #В скобках указываем путь к chromedriver.exe
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

#Вход в Вконтакте
    def test_login(self):
        self.driver.get("http://www.vk.com")
        self.assertTrue(self.driver.find_element(*MainPageLocators.LOGIN_FIRST).is_displayed)
        self.driver.find_element(*MainPageLocators.LOGIN_FIRST).send_keys('solomon.testirovanie@mail.ru')
        self.assertTrue(self.driver.find_element(*MainPageLocators.PASS_FIRST).is_displayed)        
        self.driver.find_element(*MainPageLocators.PASS_FIRST).send_keys('qwe123asd')
        self.assertTrue(self.driver.find_element(*MainPageLocators.FOREIGN_COMP_FIRST).is_displayed)        
        self.driver.find_element(*MainPageLocators.FOREIGN_COMP_FIRST).click()
        self.assertTrue(self.driver.find_element(*MainPageLocators.GO_BUTTON_FIRST).is_displayed)         
        self.driver.find_element(*MainPageLocators.GO_BUTTON_FIRST).click()
#Выход из Вконтакте
        self.assertTrue(self.driver.find_element(*MainPageLocators.OPTION_FIRST).is_displayed)                 
        self.driver.find_element(*MainPageLocators.OPTION_FIRST).click()
        self.assertTrue(self.driver.find_element(*MainPageLocators.OUT_FIRST).is_displayed)                 
        self.driver.find_element(*MainPageLocators.OUT_FIRST).click()

#Вход в Вконтакте с ошибочным логином и паролем
    def test_login_false(self):
        self.driver.get("https://vk.com/login?act=mobile&hash=e4ce14a2a6a7de18")
        self.assertTrue(self.driver.find_element(*MainPageLocators.LOGIN_AFTER_OUT).is_displayed)        
        self.driver.find_element(*MainPageLocators.LOGIN_AFTER_OUT).send_keys('salomon.testirovanie@mail.ru')
        self.assertTrue(self.driver.find_element(*MainPageLocators.PASS_AFTER_OUT).is_displayed)        
        self.driver.find_element(*MainPageLocators.PASS_AFTER_OUT).send_keys('qwe1234asd4')
        self.assertTrue(self.driver.find_element(*MainPageLocators.FOREIGN_COMP_AFTER_OUT).is_displayed)                
        self.driver.find_element(*MainPageLocators.FOREIGN_COMP_AFTER_OUT).click()
        self.assertTrue(self.driver.find_element(*MainPageLocators.GO_BUTTON_AFTER_OUT).is_displayed)                        
        self.driver.find_element(*MainPageLocators.GO_BUTTON_AFTER_OUT).click()
#Ввод корректного логина и вход
        self.assertTrue(self.driver.find_element(*MainPageLocators.LOGIN_AFTER_INCORRECT).is_displayed)                                
        self.driver.find_element(*MainPageLocators.LOGIN_AFTER_INCORRECT).clear()                                        
        self.driver.find_element(*MainPageLocators.LOGIN_AFTER_INCORRECT).send_keys('solomon.testirovanie@mail.ru')
        self.assertTrue(self.driver.find_element(*MainPageLocators.PASS_AFTER_INCORRECT).is_displayed)                                        
        self.driver.find_element(*MainPageLocators.PASS_AFTER_INCORRECT).send_keys('qwe123asd')
        self.assertTrue(self.driver.find_element(*MainPageLocators.GO_BUTTON_AFTER_INCORRECT).is_displayed)                                        
        self.driver.find_element(*MainPageLocators.GO_BUTTON_AFTER_INCORRECT).click()        
#Выход из Вконтакте
        self.assertTrue(self.driver.find_element(*MainPageLocators.OPTION_FIRST).is_displayed)                                                
        self.driver.find_element(*MainPageLocators.OPTION_FIRST).click()
        self.assertTrue(self.driver.find_element(*MainPageLocators.OUT_FIRST).is_displayed)                                                        
        self.driver.find_element(*MainPageLocators.OUT_FIRST).click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
