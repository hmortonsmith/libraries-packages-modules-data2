# Modules
# we have been creating asnd importing modules
# modules abstract functionality
# can be complex or simple and might depend on exteranal libraries

import os

working_dir = os.getcwd()
print(working_dir)


def return_login_user():
    return os.getlogin()


def encode_file(file_name):
    return os.fsencode(file_name)


def decode_file(file_name):
    return os.fsdecode(file_name)
