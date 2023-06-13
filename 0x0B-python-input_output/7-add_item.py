#!/usr/bin/python3
""" 7-add_item module """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

with open("add_item.json", 'a', encoding="utf-8") as f:
    pass
with open("add_item.json", 'r', encoding="utf-8") as f:
    copy = f.read()
if copy:
    myList = load_from_json_file("add_item.json")
else:
    myList = []
for args in sys.argv[1:]:
    myList.append(args)
save_to_json_file(myList, "add_item.json")
