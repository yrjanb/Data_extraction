import tkinter as tk #tkinter is used to create the graphical user interface.
import system_info_export as sie #imported custom script for system information
import ipconfig_all_export as iae #imported custom script for nettwork information
import dxdiag_export as dx
import msinfo32_report_export as msinfo

root = tk.Tk() #root window



ip_checked = tk.IntVar() #integer value to validate if checkbox is checked or not
system_checked = tk.IntVar()#integer value to validate if checkbox is checked or not
dxdiag_checked = tk.IntVar()#integer value to validate if checkbox is checked or not
msinfo32_checked = tk.IntVar()#integer value to validate if checkbox is checked or not


def check_checkbox(): #Function to go through which of the checkboxes are active
	if ip_checked.get() == 1 and system_checked.get() ==1:
		iae.ipconfig_obj()
		label1 = tk.Label(root, text='Network information has been exported')
		label1.grid(row=0,column=1)
		
		sie.systeminfo_obj()
		label2 = tk.Label(root, text='System information has been exported')
		label2.grid(row=1,column=1)

		dx.dxdiag_obj()
		label2 = tk.Label(root, text='System information has been exported')
		label2.grid(row=2,column=1)

		msinfo.msinfo32_obj()
		label2 = tk.Label(root, text='MSinfo information has been exported')
		label2.grid(row=3,column=1)


	elif ip_checked.get() == 1:
		iae.ipconfig_obj()
		label1 = tk.Label(root, text='Network information has been exported')
		label1.grid(row=0,column=1)
	elif system_checked.get() == 1:
		sie.systeminfo_obj()
		label2 = tk.Label(root, text='System information has been exported')
		label2.grid(row=1,column=1)
	elif dxdiag_checked.get() == 1:
		dx.dxdiag_obj()
		label2 = tk.Label(root, text='DXDIAG information has been exported')
		label2.grid(row=2,column=1)
	elif msinfo32_checked.get() == 1:
		msinfo.msinfo32_obj()
		label2 = tk.Label(root, text='MSinfo information has been exported')
		label2.grid(row=3,column=1)
	else:
		print('nothing is selected!') #Added for troubleshooting


checkbox1 = tk.Checkbutton(root, text="ipconfig /all", onvalue = 1, offvalue = 0,
			variable = ip_checked).grid(row=0,column=0, sticky="W")
checkbox2 = tk.Checkbutton(root, text="Info", onvalue = 1, offvalue = 0,
			variable = system_checked).grid(row=1,column=0, sticky="W")
checkbox3 = tk.Checkbutton(root, text="DXDIAG", onvalue = 1, offvalue = 0,
			variable = dxdiag_checked).grid(row=2,column=0, sticky="W")
checkbox4 = tk.Checkbutton(root, text="MSinfo32", onvalue = 1, offvalue = 0,
			variable = msinfo32_checked).grid(row=3,column=0, sticky="W")

# label1 = tk.Label(root, text='File has bee exported')(row=0,column=2).grid(row=0,column=2)

button1 = tk.Button(root, text='Extract!', command = check_checkbox).grid(row=5,column=1)


root.title('Data Extraction') #This where one defines what is the program name
root.geometry("400x150") #Width x Height
root.mainloop() #program loop to keep it running

