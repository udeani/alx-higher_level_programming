#!/usr/bin/python3
def search_replace(my_list, search, replace):
    "Function to replace occurrences fo an element by another in a list"
    new_list = my_list[:]
    for i in new_list:
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
