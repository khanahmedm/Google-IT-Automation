
#!/usr/bin/env python3

import re
import operator
import csv

error_counts = {}
error_users = {}
user_info = {}

# Read syslog file and check to see if the line has error or info messages
def scan_logfile():
    f = open('syslog.log', "r") 
    for line in f:
        if " ERROR " in line:
            search_for_errors(line)
            add_users(line, 1)
        elif " INFO " in line:
            add_users(line, 2)
    return


# search for errors
def search_for_errors(str):
    match = re.search(r"(ERROR [\w \[]*) ", str)
    if match is not None:
        aux = match.group(0).replace("ERROR ", "").strip()
        if aux == "Ticket":
         aux = "Ticket doesn't exist"
        if not aux in error_counts:
            error_counts[aux] = 1
        else:
            error_counts[aux] += 1
    return

# add users in the error and info dictionaries
def add_users(str, op):
    match = re.search(r'\(.*?\)', str)
    user = match.group(0)
    userA = user.strip("()")
    if op == 1:
        if not userA in error_users:
            error_users[userA] = 1
        else:
            error_users[userA] += 1
    elif op == 2:
        if not userA in user_info:
            user_info[userA] = 1
        else:
            user_info[userA] += 1
    return

# sort dictionary
def sort_dict(op, d):
    if op == 1:
        s = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    elif op == 2:
        s = sorted(d.items(), key=operator.itemgetter(0))
    return s

def get_error(key1):
    for key, value in error_users:
        if key is key1:
            return value
    return 0

# write to csv files
def write_to_csvfile(op):
    if op == 1:
        with open('user_statistics.csv', 'w', newline='') as output:
            fieldnames = ['Username', 'INFO', 'ERROR']
            csvw = csv.DictWriter(output, fieldnames=fieldnames)
            csvw.writeheader()
            for key, value in user_info:
                valError = get_error(key)
                csvw.writerow({'Username': key, 'INFO': value, 'ERROR': valError})
    if op == 2:
        with open('error_message.csv', 'w', newline='') as output:
            fieldnames = ['Error', 'Count']
            csvw = csv.DictWriter(output, fieldnames=fieldnames)
            csvw.writeheader()
            for key, value in error_counts:
                csvw.writerow({'Error': key, 'Count': value})
    return

# initialize dictionary with zero counts as values
def initialize_dict():
    for user in error_users.keys():
        if user not in user_info:
            user_info[user] = 0
    for user in user_info.keys():
        if user not in error_users:
            error_users[user] = 0
    return


scan_logfile()
initialize_dict()
error_counts = sort_dict(1, error_counts)
error_users = sort_dict(2, error_users)
user_info = sort_dict(2, user_info)
write_to_csvfile(1)
write_to_csvfile(2)
