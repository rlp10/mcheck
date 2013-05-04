#!/usr/bin/env python2

# TODO
# think about movies
# think about music

from __future__ import print_function
import argparse
import os
import pdb
import sys

def print_error(filename, reason):
    print("{} ({})".format(filename, reason))

def is_folder(path):
    '''Expecting folder, not file'''
    return not os.path.isfile(path)

def is_file(path):
    '''Expecting file, not directory'''
    return os.path.isfile(path)

def begins_season(path):
    '''Expects folder to begin "Season "'''
    fn = os.path.split(path)[1]
    return fn[0:7] == 'Season '

def has_10_characters(path):
    '''Expects file to be 10 characters long'''
    fn = os.path.split(path)[1]
    return len(fn) == 9

def ends_two_digits(path):
    '''Expects 8th and 9th characters to be numbers'''
    fn = os.path.split(path)[1]
    try:
        int(fn[8:9])
        return True
    except:
        return False

def begins_s(path):
    '''Expecting filename to begin with "s"'''
    return os.path.split(path)[1].startswith("S")

def contains_e(path):
    '''Expects 4th character to be "e"'''
    fn = os.path.split(path)[1]
    return fn[3] == 'E'

def check_season_numbers(path):
    '''Expecting second and third digits to be integers'''
    fn = os.path.split(path)[1]
    try:
        int(fn[1:2])
        return True
    except:
        return False

def check_episode_number(path):
    '''Expects 5th and 6th characters to be digits'''
    fn = os.path.split(path)[1]
    try:
        int(fn[4:5])
        return True
    except:
        return False

def check_episode_name(path):
    '''Expects 7th character to be space and name between 8th character and dot'''
    fn = os.path.split(path)[1]
    try:
        assert fn[6] == ' '
        position = fn.index('.')
        assert position > 7
        return True
    except:
        return False

def check_directory(check_list, path):
    files = os.listdir(path)
    for file in files:
        for check_func in check_list:
            if not check_func(os.path.join(path, file)):
                print_error(os.path.join(path, file), check_func.__doc__)

def check_tv_folder(path):
    check_directory([ is_folder ], path)
    dirs = [ entry for entry in os.listdir(path) if not os.path.isfile(os.path.join(path, entry)) ]
    for dir in dirs:
        check_seasons_folder(os.path.join(path, dir))

def check_seasons_folder(path):
    check_directory([ is_folder, begins_season, ends_two_digits, has_10_characters ], path)
    for dir in os.listdir(path):
        if not os.path.isfile(os.path.join(path, dir)):
            check_episodes_folder(os.path.join(path, dir))

def check_episodes_folder(path):
    check_directory([ is_file, begins_s, check_season_numbers, contains_e, check_episode_number, check_episode_name], path)

def main():
    parser = argparse.ArgumentParser(description='checks media folders')
    parser.add_argument('subcommand', help='subcommand: tv, seasons or episodes')
    parser.add_argument('path', help='folder to check')
    args = parser.parse_args()
    if args.subcommand == 'tv':
        check_tv_folder(args.path)
    elif args.subcommand == 'seasons':
        check_seasons_folder(args.path)
    elif args.subcommand == 'episodes':
        check_episodes_folder(args.path)
    else:
        print('subcommand unknown')
        exit(1)

if __name__ == '__main__':
    main()
