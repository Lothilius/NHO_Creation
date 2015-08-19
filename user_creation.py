__author__ = 'Lothilius'

import numpy as np
import sys
import csv
from lookup_db import *
from actions import *
from SFDC_User import *
import string
import random


# TODO Make a class for the profile

# Get user information from CSV file
def array_from_file(filename):
    """Given an external file containing data,
            create an array from the data.
            The assumption is the top row contains column
            titles.
    """
    data_array = []
    with open(filename, 'rU') as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for row in spam_reader:
            data_array.append(row)

    data_array = np.array(data_array)

    return data_array


def main():
    #TODO fix user interaction lines
    while True:
        environment = raw_input("Which environment would you like to use, (prod) or (st)aging? ")
        if environment == 'prod':
            username, pw = salesforce_login_production()
        elif environment == ('st' or 'staging'):
            username, pw = salesforce_login_staging()
        else:
            print "I'm Sorry I did not understand your selection. Please try again."

        mode = raw_input('Would you like (s)ingle, (a)ssisted, or (f)ull automatic provisioning mode? ')
        if mode == ('s' or 'single'):
            new_user_name = raw_input('Please enter name: ')
            new_user_title = raw_input('Please enter title: ')
            new_user_manager = raw_input('Please enter manager: ')
            user = SfdcUser()
            user.add_name(new_user_name)
            user.add_title(new_user_title)
            user.add_manager(new_user_manager)
            print user.email()
            start_form_fill(environment, user.first_name, user.last_name, user.email(), user.name(), user.title,
                            user.manager)

        elif mode == ('a' or 'assisted'):
            file_name = raw_input('Please enter file name: ')
            full_file_path = '/Users/martin.valenzuela/Desktop/SFDC_exports/New_hires_' + file_name + '.csv'  # New_hires
            csv_info = array_from_file(full_file_path)

            for each in csv_info[12:]:
                # Create User object for each user row in csv
                user = SfdcUser()
                user.add_name(each[1])
                user.add_title(each[2])
                user.add_manager(each[3])
                print user.email()
                start_form_fill(environment, user.first_name, user.last_name, user.email(), user.name(), user.title,
                                user.manager)

        elif mode == ('f' or 'full'):
            file_name = raw_input('Please enter file name: ')
            full_file_path = '/Users/martin.valenzuela/Desktop/SFDC_exports/New_hires_7_23' + file_name + '.csv'  # New_hires
            csv_info = array_from_file(full_file_path)
            # print csv_info[1, 2]

            user = SfdcUser()
            user.add_name(csv_info[1, 2])
            print csv_info[1, 2]

        else:
            print "I'm Sorry I did not understand your selection. Please try again."

            #print user_list.name()



    # try:
    #     login(browser)
    #     browser.implicitly_wait(15)
    # except common.exceptions.ElementNotVisibleException:
    #     browser.implicitly_wait(3)
    #     login(browser)
    #     browser.implicitly_wait(15)
    #
    # for each in user_list:
    #     if each[3] == 'Contractor':
    #         create_user(each[0], each[1], each[2], each[2], '100500000000D6z', '00e50000001BrAN')
    #         print each
    #     else:
    #         pass
    #     # create_user(each)


main()




