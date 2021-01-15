import sys
import argparse
import json
from os import path
import re
import numpy as np
from git import Repo
# with open('version.txt') as json_file:
#     data = json.load(json_file)
#     for p in data['version']:
#         print('Name: ' + p['name'])
#         print('Website: ' + p['website'])
#         print('From: ' + p['from'])
#         print('')

def openJson():
    try:
        f = open(".versions.txt")
        with f as json_file:
            return json.load(json_file)
    except IOError:
        print("No file found")
        # data['version'] = []
        # data['version'].append( {
        # 'major': 0,
        # 'minor': 0,
        # 'bug': 0,
        # 'changelog': '',
        # })


# def main(d):
#     #data = openJson()
#     data['version'].insert(0,d)
#     # data['version'].insert(0, {
#     #     'major': 3,
#     #     "minor": 0,
#     #     "bug": 0,
#     #     # 'version_number': '2.0.0',
#     #     'changelog': 'This is a test',
#     # })
#     with open('.versions.txt', 'w') as outfile:
#         json.dump(data, outfile)

def check(s):
    if s: 
        return s.split(',')


def version(major = [], minor = [], bug = []):
    major = check(major)
    minor = check(minor)
    bug = check(bug)
    new_version =[len(major) if major else 0, len(minor) if minor else 0, len(bug) if bug else 0]
    data = {}
    data['version'] = []

    if path.exists('.versions.txt'):
        data = openJson()
        version = np.array([data['version'][0]['major'], data['version'][0]['minor'], data['version'][0]['bug']])
        this_version = np.array([len(major) if major else 0, len(minor) if minor else 0, len(bug) if bug else 0])
        new_version = np.add(version, this_version)
    
    changelog = "Major: %s Minor: %s Bug: %s" % (major, minor, bug)


    new_insert = {
        'major': int(new_version[0]),
        "minor": int(new_version[1]),
        "bug": int(new_version[2]),
        'changelog': changelog,
    }

    data['version'].insert(0,new_insert)
    with open('.versions.txt', 'w') as outfile:
        json.dump(data, outfile)
    # main(data)
    


parser = argparse.ArgumentParser(description='Handles pushing to repo')
parser.add_argument('-M', help='Submits a Major change')
parser.add_argument('-m', help='Submits a Minor change')
parser.add_argument('-b', help='Submits a bugfix')
args = parser.parse_args()
version(major=args.M, minor=args.m, bug=args.b)