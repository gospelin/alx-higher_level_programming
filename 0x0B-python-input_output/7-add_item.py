#!/usr/bin/python3

""" Module that adds all arguments to a Python list, and then
save them to a file
"""

from sys import argv
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

my_list = []

if os.path.exists(filename):
    if os.path.getsize(filename) == 0:
        my_list = []
    else:
        my_list = load_from_json_file(filename)

for args in argv[1:]:
    my_list.append(args)

save_to_json_file(my_list, filename)
