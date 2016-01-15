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
    # TODO fix user interaction lines
    while True:
        mode = raw_input('Would you like (s)ingle, (a)ssisted, or (f)ull automatic provisioning mode? ')
        if mode == ('s' or 'single'):
            new_user_name = raw_input('Please enter name: ')
            user = SfdcUser()
            user.add_name(new_user_name)
            print user.email()
            okta_load(user.first_name, user.last_name)

        elif mode == ('a' or 'assisted'):
            file_name = raw_input('Please enter file name: ')
            while file_name != 'exit':
                try:
                    full_file_path = '/Users/martin.valenzuela/Desktop/SFDC_exports/' + file_name + '.csv'  # New_hires
                    csv_info = array_from_file(full_file_path)
                    break
                except IOError:
                    print """\nNo file found with that name. \nPlease Try again. \n"""
                    file_name = raw_input('Please enter file name: ')

            for each in csv_info[1:]:
                # wait(10)
                if 'should already' not in each[0]:
                    print each[0]
                    # Create User object for each user row in csv
                    user = SfdcUser()
                    user.add_name(each[0])
                    print user.email()
                    okta_load(user.first_name, user.last_name)

        elif mode == ('f' or 'full'):
            file_name = raw_input('Please enter file name: ')
            full_file_path = '/Users/martin.valenzuela/Desktop/SFDC_exports/' + file_name + '.csv'  # New_hires
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



