#only import needed inorder to run command prompt and to output to file.
import os

#This is a simple script that prints out the nettwork information of the Windows computer that it is run on.
#This is part of other smaller scripts which is inteded to be used with the GUI.
#However, it can be used as a standalone to obtain neccessary system information and/or report.

def msinfo32_obj():
	try:os.system('cmd /c "msinfo32 /report \\Users\\%USERNAME%\\Desktop\\msinfo32_report.txt"')
		#opens command prompt
		# /c means that it closes cmd after running, change to "/k" if one wants to keep cmd open.
		#larger than means that it will be "output to" and then the filename and destination is given.
	except:
		print('could not execute command')
		#Exception included for troubleshooting


