mcheck
======

This program checks the format of folders and files containing media.  Currently, it only works with television episodes, although music and movies will be added shortly.

Specification
-------------

All television media should be held in a single directory.  In that directory, there should be no files, only directories, with each being named after a single television series.

Within each of those series folders, there should be a list of directories, each called 'Season XX' where XX are digits representing the series number.

Within each of thse folders, should be a list of episodes, each of the form 'SXXEXX episode name.XXX' with the apropriate season number, episode number, episode name and file extension.

Usage
-----

Currently, only the following subcommands work:

mcheck tv <path> - checks multiple series from specified path

mcheck seasons <path> - checks multiple seasons of one series from specified path

mcheck episodes <path> - checks single season at specified path

