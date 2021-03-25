import os
import sys

#This is a simple script that prints out the system information of the Windows computer that it is run on.
#This is part of other smaller scripts which is inteded to be used with the GUI.
#However, it can be used as a standalone to access system information.


#Gets username credentials
logged_in_user = os.getlogin() 

#Set path variable
path = f"C:\\Users\\{logged_in_user}\\AppData\\Roaming\\Microsoft\\Windows\\Recent\\"

#Lists the contents of the directory and saves it in the variable
recent_file_list = os.listdir(path)

#Print statement to see if separation with newline works (for testing only)
# print (*recent_file_list, sep = "\n") #(for testing only)

# joined_string = "\n".join(test) #1

# print (joined_string) #1

with open('recent_files_current_user.txt', 'w') as f: #Creating a file and giving it Write privileges
    # print("User: ",logged_in_user,'\n',joined_string, file=f) #1 #Printing the information to file, but adds a weir space before the files
    print (logged_in_user,'\n',*recent_file_list, sep = "\n", file=f) #Printing the information to file

