import os #imports the OS module


dir_path = os.path.dirname(os.path.realpath(__file__)) #gets the path name from where the script is run

loc = dir_path[0:2] #stores the value of the first three characters such as "C:\"