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
Created by Chris Dewing

Last Edited: 6/12/19

Version 2.1:
-Added Gmail check test case
-Added Allure Decorators
-Checked spelling 
-Fixed spacing issues
-Class name changed from test_class to MainTest
-Added negative test case

Details:
The program runs through various actions that can be performed on the iLINK Dev website. In addition, 
the program will output an Allure report that details what tests were performed and the results of those tests.

Note that when using unittest, the methods have to be in numerical or alphabetic order.
If they are not in numerical or alphabetic order, the methods will run out of order in the class. This is why each
method in the class starts off as test_'letter'...
 
'''

@allure.story('[Conversation] - Automate  the  Signin  screen across all three apps')
@allure.feature('Web App SigninPage Tests')

#There are 9 functions in this class that test different actions of iLINK Dev
class MainTest(unittest.TestCase):

    #This function logs the user into iLINK Dev
    @allure.testcase("Test1")
    @allure.description("This function logs the user into iLINK Dev")
    @allure.title("Login")
    @allure.severity("Critical")
    @allure.testcase("Validate Login")
    @allure.step("Login to iLINK Dev using username and password")
    def test_a_login(self):
        Browser_Management.open_browser("gc", "http://ilinkdev.ilabquality.com/")
        Login = Login_Class(Global_Variables.global_Driver)
        Login.input_username("xpath", '//*[@id="user"]', "CDewingAdmin")
        Login.input_password("xpath", '//*[@id="pass"]', "p!9%ni!EOb2wdBpz*)QdrAOQ")
        Login.click_login_button("xpath", '//*[@id="wp-submit"]')



    #This function clicks through each menu button option with a 2 second pause in between
    #The test then scrolls to the bottom of the page after clicking the Chat button
    @allure.testcase("Test2")
    @allure.description("This function clicks through each menu button option with a 2 second pause in between \n"
                        " The test then scrolls to the bottom of the page after clicking the Chat button")
    @allure.title("Menu Navigation")
    @allure.step("Click through the Menu Buttons on the iLINK Dev website")
    def test_b_menu_navigation(self):
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
    #Lastly, the function clicks the revision button, scrolls to the bottom of the page,and clicks on the Dashbaord page
    @allure.testcase("Test3")
    @allure.description("This function uses the iLINK Dev main search to search for iTEST.\n"
                        " The function then navigates through 9 pages of the iTEST method description. \n "
                        "Lastly, the function clicks the revision button, scrolls to the bottom of the page,and "
                        "clicks on the Dashbaord page")
    @allure.title("Search For iTEST Description")
    @allure.step("Search for iTEST and then click through 9 of the Read Me slides")
    def test_c_search_itest(self):
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
    #A Gmail email will then be sent to that user informing them that a message was sent via iLINK Dev.
    #The last test case in this class will open Gmail so the user can see if an email was received.
    @allure.testcase("Test4")
    @allure.description("This function searches for a member in iLINK and clicks through the menu options for that"
                        " selected user. \n The function then clicks on message button and sends a message to the same"
                        " user that was searched for. \n A Gmail email will then be sent to that user informing them "
                        "that a message was sent via iLINK Dev.")
    @allure.title("Search for an iLAB Employee")
    @allure.step("Search for an iLAB employee and send a message to that same employee ")
    def test_d_member_search(self):
        locator = Locators(Global_Variables.global_Driver)
        locator.click_element("linktext", "Members")
        locator.send_text("id", "members_search", "Chris Dewing")
        time.sleep(1)
        locator.click_element("xpath", "/html/body/div[2]/section/div/header/div[1]/form/button/i")
        time.sleep(2)
        locator.click_element("xpath", "/html/body/div[2]/section/div/div/div/article/div/form/div/div/ul/li/div"
                                       "[2]/div[1]/a/h3")
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
        locator.click_element("xpath","/html/body/div[2]/section/div/div/div/article/div/div[1]/div[2]/div/div[2]"
                                      "/div[2]/a")
        time.sleep(2)
        locator.send_text("xpath", "//*[@id='subject']", "Test Subject Line")
        time.sleep(2)
        locator.send_text("xpath", "//*[@id='message_content']", "Test message line")
        time.sleep(2)
        locator.click_element("id", "send")


    #This function edits a selected users's profile by adding a new cell phone number
    @allure.testcase("Test5")
    @allure.description("This function edits a selected users's profile by adding a new cell phone number")
    @allure.title("Edit iLAB Employee Profile")
    @allure.step("Click the edit view of the employee profile and change the phone number to (555)555-5555")
    def test_e_user_profile(self):
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
    @allure.description("This function checks to see if the user has any notifications.")
    @allure.title("Check Notifications")
    @allure.step("Click the bell icon and see if there are any notifications")
    def test_f_menu_navigation2(self):
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
    @allure.description("This functions attempts to submit a survey and IT help desk request without filling out all "
                        "information.\n The system should highlight red indicating what fields need to still be filed "
                        "out before submitting.")
    @allure.title("Submit Incomplete Survey and IT Help Desk Request")
    @allure.step("On the main page, fill out one line of the survey and IT support box, then click submit on both")
    def test_g_submit_issue_error(self):
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

    #This function opens up the Gmail account that the iLINK message was sent to
    #The inbox of that Gmail account should show that a message was received from iLINK DEV
    @allure.testcase("Test8")
    @allure.description("This function opens up the Gmail account that the iLINK message was sent to \n"
                        " The inbox of that Gmail account should show that a message was received from iLINK DEV")
    @allure.title("Open Gmail")
    @allure.step("Open Gmail and verify that the email was received from iLINK ")
    def test_h_check_gmail(self):
        Browser_Management.open_browser("gc", "https://gmail.com")
        Login = Login_Class(Global_Variables.global_Driver)
        Login.input_username("id","identifierId","chris.dewing@ilabquality.com")
        Login.click_login_button("xpath", "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]"
                                          "/div/span/span")
        Login.input_password("xpath", "//*[@id='password']/div[1]/div/div[1]/input", "The199329hill")
        Login.click_login_button("xpath", "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div"
                                          "[1]/div/span/span")
        time.sleep(3)

    #This function will attempt to click the xpath of an element that doesn't exist on the homepage of Gmail
    @allure.testcase("Test9")
    @allure.title("Fail Test Case")
    @allure.severity("Low")
    @allure.description("This function will attempt to click the xpath of an element that doesn't exist on the "
                        "homepage of Gmail")
    @allure.step("Test case will automatically fail")
    def test_i_fail(self):
        locator = Locators(Global_Variables.global_Driver)
        locator.click_element("xpath", "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]"
                                          "/div/span/span" )




    if __name__ == '__main__':
        unittest.main(verbosity=2)
