from iLAB_US_Framework.Global import Global_Variables
from iLAB_US_Framework.Global import Objects
from iLAB_US_Framework.iLAB_Selenium import Browser_Management
from iLAB_US_Framework.iLAB_Selenium import Login
from iLAB_US_Framework.iLAB_Selenium.Locator import Locators

from iLAB_US_Framework.iLAB_Selenium import Wait_Until
from iLAB_US_Framework.iLAB_Selenium.Login import Login_Class
import time
import unittest
import allure
import pytest

'''
Note that when using unittest, the methods have to be in numerical or alphabetic order.
If the are not in numerical or alphabetic order, the methods will run out of order in the class.
 
'''



@allure.story('[Conversation] - Automate  the  Signin  screen across all three apps')
@allure.feature('Web App SigninPage Tests')

#There are 7 functions in this class that test different actions of iLINK Dev
class test_class(unittest.TestCase):

    #This function logs the user into iLINK Dev
    @allure.testcase("Test1")
    def test_a_login(self):
        Browser_Management.open_browser("gc", "http://ilinkdev.ilabquality.com/")
        Login = Login_Class(Global_Variables.global_Driver)
        Login.input_username("xpath", '//*[@id="user"]', "CDewingAdmin")
        Login.input_password("xpath", '//*[@id="pass"]', "p!9%ni!EOb2wdBpz*)QdrAOQ")
        Login.click_login_button("xpath",'//*[@id="wp-submit"]')


    #This function clicks through each menu button option with a 2 second pause in between
    @allure.testcase("Test2")
    def test_a_menu_navigation(self):
        locator = Locators(Global_Variables.global_Driver)
        locator.click_element("linktext", "Global Events")
        time.sleep(2)
        locator.click_element("linktext", "Groups")
        time.sleep(2)
        locator.click_element("linktext", "Chat")
        time.sleep(2)
        locator.scroll_to_bottom_of_page()
        time.sleep(2)
        locator.click_element("linktext", "Members")
        time.sleep(2)
        locator.click_element("linktext", "Posts")
        time.sleep(2)
        locator.click_element("linktext", "Wiki")
        time.sleep(2)
        locator.click_element("linktext", "Dashboard")
        time.sleep(2)


    #This function uses the iLINK Dev main search to search for iTEST.
    #The function then navigates through 9 pages of the iTEST method description.
    #Lastly, the function clicks the revision button, scrolls to the bottom of the page,and clicks on the dashbaord page
    @allure.testcase("Test3")
    def test_b_search_itest(self):
        locator = Locators(Global_Variables.global_Driver)
        locator.click_element("xpath", "/html/body/div[2]/header/nav/div[2]/a[1]/i")
        locator.send_text("id", "s", "iTEST")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/header/div[3]/div/form/button/i")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/article[1]/div[2]/div[2]/a")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/article/div[2]/div[1]/div/a[2]")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/article/div[2]/div[1]/div/a[2]")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/article/div[2]/div[1]/div/a[2]")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/article/div[2]/div[1]/div/a[2]")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/article/div[2]/div[1]/div/a[2]")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/article/div[2]/div[1]/div/a[2]")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/article/div[2]/div[1]/div/a[2]")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/article/div[1]/div/ul/li[4]/a")
        locator.scroll_to_bottom_of_page()
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/footer/div[1]/div/div/div[2]/div/ul/li[1]/a")


    #This function searches for a member in iLINK and clicks through the menu options for that selected user.
    #The function then clicks on message button and sends a message to the same user that was searched for.
    #A Gail email will then be sent to that user informing them that a message was sent via iLINK Dev.
    @allure.testcase("Test4")
    def test_c_member_search(self):
        locator = Locators(Global_Variables.global_Driver)
        locator.click_element("linktext", "Members")
        locator.send_text("id", "members_search", "Chris Dewing")
        time.sleep(1)
        locator.click_element("xpath", "/html/body/div[2]/section/div/header/div[1]/form/button/i")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/article/div/form/div/div/ul/li/div[2]/div[1]/a/h3")
        time.sleep(2)
        locator.click_element("id", "user-xprofile")
        time.sleep(2)
        locator.click_element("id", "user-notifications")
        time.sleep(2)
        locator.click_element("id", "user-messages")
        time.sleep(2)
        locator.click_element("id", "user-groups")
        time.sleep(2)
        locator.click_element("id", "user-activity")
        time.sleep(3)
        locator.click_element("id", "user-messages")
        time.sleep(2)
        locator.click_element("xpath","/html/body/div[2]/section/div/div/div/article/div/div[1]/div[2]/div/div[2]/div[2]/a")
        time.sleep(2)
        locator.send_text("xpath", "//*[@id='subject']","Test Subject Line")
        time.sleep(2)
        locator.send_text("xpath", "//*[@id='message_content']", "Test message line")
        time.sleep(2)
        locator.click_element("id", "send")

    
    #This function edits a selected users's profile by adding a new cell phone number
    @allure.testcase("Test5")
    def test_d_user_profile(self):
        locator = Locators(Global_Variables.global_Driver)
        locator.click_element("id", "user-thumb")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/header/div[1]/div[1]/div/nav/ul/li[2]/a")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/header/div[1]/div[1]/div/nav/ul/li[2]/ul/li[2]/a")
        time.sleep(2)
        locator.send_text("xpath", "//*[@id='field_12']", "(555)-555-5555")
        time.sleep(2)
        locator.click_element("xpath", "//*[@id='profile-group-edit-submit']")
        time.sleep(2)
        locator.click_element("linktext", "Dashboard")

    #This function checks to see if the user has any notifications.
    @allure.testcase("Test6")
    def test_e_menu_navigation2(self):
        locator = Locators(Global_Variables.global_Driver)
        locator.click_element("linktext", "Posts")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/div[1]/div[2]/div[1]/a/picture/img")
        locator.scroll_to_bottom_of_page()
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/footer/div[1]/div/div/div[2]/div/ul/li[1]/a")
        time.sleep(1)
        locator.click_element("id", "nav-notification-trigger")
        time.sleep(2)
        locator.click_element("id", "nav-notification-trigger")


    #This functions attempts to submit a survey and IT help desk request without filling out all information.
    #The system should highlight red indicating what fields need to still be filed out before submitting.
    @allure.testcase("Test7")
    def test_f_submit_issue_error(self):
        locator = Locators(Global_Variables.global_Driver)
        time.sleep(1)
        locator.click_element("xpath", "//*[@id='fld_8949845_2']")
        time.sleep(2)
        locator.send_text("xpath", "//*[@id='fld_185917_1']", "Test")
        time.sleep(3)
        locator.click_element("xpath", "//*[@id='fld_7167496_1']")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/div/div[7]/div/ul/li[5]/div[2]/div[1]/a")
        locator.scroll_to_bottom_of_page()
        locator.scroll_to_element("linktext", "Dashboard")
        locator.click_element("linktext", "Wiki")
        locator.click_element("linktext", "Dashboard")


        





    if __name__ == '__main__':
        unittest.main(verbosity=2)
