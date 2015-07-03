__author__ = 'Lothilius'

import re
import numpy as np


class SfdcUser(object):
    """ This module creates a SFDC user from the first and last name and Profile.
    """

    def __int__(self, first_name, last_name, title, profile, permissions):
        """Create an empty User Object"""
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.profile = profile
        self.permissions = permissions

    def __str__(self):
        return "[", self.first_name, " ", self.last_name, " ", self.title, " ", self.profile, " ", self.permissions

    def first_name(self):
        return self.first_name

    def last_name(self):
        return self.last_name

    def title(self):
        return self.title

    def email(self):
        return self.first_name, '.', self.last_name, '@bazaarvoice.com'

    def profile(self):
        return self.profile

    def permissions(self):
        return self.permissions

    def is_empty(self):
        return not self._user

    # Split First and Last Name
    def add_name(self, the_name):
        the_name = self.clean_name(the_name)
        the_name = the_name.split(' ')
        self.first_name = the_name[0]
        self.last_name = the_name[1]

    def add_profile_id(self, user_info):
        for i in session.query(Profiles.id).order_by(desc(Profiles.id)).limit(100):
                    user_info.append(i)

    # Clean up the Data so that consultants are caught
    def clean_name(self, the_name):
        # Remove [C]
        regex = re.compile(' \[C\]')
        the_name = regex.sub('', the_name)

        return the_name

    # Create clean array
    def create_clean(csv_info):

        user_list = np.array([['first', 'last']])
        name_list = csv_info[1:, 2]

        for each in name_list:
            name = clean_name(each)
            if name == '':
                pass
            else:
                first, last = split_name(name)
                user_list = np.append(user_list, [[first, last]], 0)

        # Get rid of the column labels first and last
        user_list = user_list[1:]
        emails = np.array([])

        # Create email column
        for each in user_list:
            email = createuser_email(each)
            emails = np.append(emails, [email], 0)

        # Join name array with email column
        user_list = np.c_[user_list, emails]

        # TODO link up with the title mapping
        # Add the first name last name and title in to one array
        user_list = np.c_[user_list, csv_info[1:-1, 3]]

        return user_list