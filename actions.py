__author__ = 'Lothilius'

from selenium import webdriver, common
from selenium.webdriver.support.select import Select
from authentication import *
import sys


def start_form_fill(environment, first_name, last_name, email, user_name, title, manager):
    if environment == 'prod':
        username, pw = salesforce_login_production()
        baseurl = "https://na3.salesforce.com/005?retURL=%2Fui%2Fsetup%2FSetup%3Fsetupid%3DUsers&setupid=ManageUsers"
    elif environment == ('st' or 'staging'):
        username, pw = salesforce_login_staging()
        baseurl = "https://cs13.salesforce.com/005?retURL=%2Fui%2Fsetup%2FSetup%3Fsetupid%3DUsers&setupid=ManageUsers"

    browser = webdriver.Chrome('/Users/martin.valenzuela/Dropbox/Coding/BV/chromedriver')
    browser.get(baseurl)
    browser.implicitly_wait(4)
    login(browser, username, pw)
    create_user(browser, first_name, last_name, email, user_name, title, manager)


# Login function
def login(browser, username, pw):
    #Write Username in Username TextBox
    browser.find_element_by_name("username").send_keys(username)

    #Write PW in Password TextBox
    browser.find_element_by_name("pw").send_keys(pw)

    #Click Login button
    browser.find_element_by_css_selector("#Login").click()

# Open the Form to create a new user.
def open_new_record(browser):
    browser.implicitly_wait(4)
    displayed = browser.find_element_by_name("new").is_displayed()
    if not displayed:
        for i in range(0, 3):
            displayed = browser.find_element_by_name("new").is_displayed()
            if displayed:
                #Click New button
                browser.find_element_by_name("new").click()
                break
            else:
                browser.implicitly_wait(3)
    else:
        browser.find_element_by_name("new").click()


# Do the actual Filling in of the form
def fill_out_form(browser, first_name, last_name, email, user_name, title, manager):
    # Set First name
    browser.find_element_by_id('name_firstName').send_keys(first_name)
    browser.implicitly_wait(1)
    # Clear and write Last name
    browser.find_element_by_id('name_lastName').clear()
    browser.find_element_by_id('name_lastName').send_keys(last_name)
    # Set Email
    browser.find_element_by_id('Email').clear()
    browser.find_element_by_id('Email').send_keys(email)

    # Clear and fill Username
    browser.find_element_by_id('Username').clear()
    browser.find_element_by_id('Username').send_keys(email)
    browser.implicitly_wait(1)

    # Clear and fill Title
    browser.find_element_by_id('Title').clear()
    browser.find_element_by_id('Title').send_keys(title)
    # Clear and fill Manager
    browser.find_element_by_id('Manager').clear()
    browser.find_element_by_id('Manager').send_keys(manager)

    # Click on Remove from notification
    browser.find_element_by_id('new_password').click()

    browser.find_element_by_id('UserPermissions_9').click()
    # Select user license
    Select(browser.find_element_by_id("user_license_id")).select_by_value('100500000000D6z')

    admin_action = ''
    while admin_action != 'Yes':
        admin_action = raw_input('Are we ready to move on? ')
    # Save
    browser.find_element_by_name("save").click()
    browser.implicitly_wait(15)


def create_user(browser, first_name, last_name, email, user_name, title, manager):
    try:
        browser.implicitly_wait(7)
        open_new_record()
    except:
        print "Unexpected error 1:", sys.exc_info()[0]
        #Wait for page to load.
        browser.implicitly_wait(10)
        browser.find_element_by_name("new").click()

    try:
        fill_out_form(browser, first_name, last_name, email, user_name, title, manager)
    except:
        print "Unexpected error 2:", sys.exc_info()[0]

    try:
        browser.implicitly_wait(15)
        displayed = browser.find_element_by_id('errorDiv_ep').is_displayed()
        print displayed
        if displayed:
            the_error = browser.find_element_by_class_name('errorMsg').text
            print 'Oh no there is an error! \n'
            print the_error
        else:
            print 'We are good!'
            browser.close()
    except common.exceptions.NoSuchElementException, e:
        print '3', e