# virtual-file-system

# User Guide for Usage:

To use the file system, execute the main.py file, now we will start from root directory.
User will be presented with the interface to select the option of the desired option and follow the procedure as guided to perform the operation.


Directory structure exists as python dictionary/dat format a directory inside directory will be separated by ‘//’ when entering path in operation options. E.g. dir1 exists and we want to create dir2 inside dir1 we will select the function from interface and type ‘dir1//dir2’


Files and their path in the function can either be given full path or relative path (after moving into a different directory)
To Move one directory behind, enter --


Caution: Only create file in the pre-existing directory, if directory doesn’t exist, create directory first, then create the file in that directory. Only on exiting by following the instructions of interface will persist the current state of file system, else if we close the program abruptly, changes wont be saved. 

# System Design:

This file system consists of 2 files, one main.py python script which is executed for functioning of the file system. One data.dat file which has limited capacity to mimic number of blocks in secondary storage and also stores the map of all the files in our system. 


In our file system, a single block is a single byte which can store a single character. 


Each directory exists as a dictionary in json file, and a sub directory is a nested dictionary in that directory/dictionary.


A file also exists in the same dictionary, but its value is a list with some meta data and page numbers of its data which exists as list within list of meta data of filename dictionary key.


Current Memory blocks are 256 for storing files data.
