from tkinter import *  
import tkinter
from search_and_filter import setVariables
from search_and_filter import switch
import tkintertable
from tkintertable import TableCanvas, TableModel
from tkinter import ttk
import controller
import sort
import get_commands_from_mic
import time

#drop down options for search and sort respectively 
OPTIONS = ["Select", "UUID", "Name", "Telecoms", "Gender", "Birth Date", "Addresses", "Marital Status", "Multiple Birth", "Communications", "Extensions", "Identifiers"]
SORTOPTIONS = ["Select", "Patient Names(A-Z)", "Age: Oldest to Youngest", "Age: Youngest to Oldest"]

app = tkinter.Tk()
variable = StringVar(app)
variable2 = StringVar(app)
rows = controller.patients
left = right = container = container2 = tableContainer = tableContainer1 = canvas1 = canvas2 = label = entryLabel = fieldLabel = searchEntry = w = None 
label1 = sortLabel = v = button = button1 = voiceButton = tv = tv1 = voicePrompts = None

def setWindow():
	global voiceButton
	global voicePrompts
	app.title("FHIRByVoice")
	app.geometry('1200x400')

	titleLabel = Label(text="Welcome to the FHIRByVoice app")
	titleLabel.config(font=("Calibri", 25))
	voiceButton = Button(canvas1, text="Voice", command=setVarsAgain)
	voicePrompts = tkinter.Entry(canvas1)
	voicePrompts.insert(0, "First Press the voice button and then say 'sort by' or 'search by'")
	titleLabel.pack()
	voiceButton.pack()
	voicePrompts.pack(fill="x")

def setDropDownVars(o1, o2):
	variable.set(OPTIONS[o1])
	variable2.set(SORTOPTIONS[o2])

#when submit for search is pressed, the selected field and criteria are processed
#to display the required data on the tables
def submit():
	searchField = variable.get()
	toSearch = searchEntry.get()
	setVariables(searchField, toSearch)
	switch(variable.get(), searchEntry.get())
	controller.showSelection(searchField, toSearch)
	onSubmit()

#similar to submit, but for sorting
def sortSubmit():
	sortField = variable2.get()
	sort.switch(sortField)
	controller.sortSelection(sortField)
	onSortSubmit()

def setContainers():
	global left, right, container, container2, tableContainer, tableContainer1, canvas1, canvas2
	left = Frame(app, borderwidth=2, relief="solid")
	right = Frame(app, borderwidth=2, relief="solid")
	container = Frame(left,relief="solid")
	container2 = Frame(right, relief="solid")
	tableContainer = Frame(left, relief="solid")
	tableContainer1 = Frame(right, relief="solid")
	canvas1 = tkinter.Canvas(container)
	canvas2 = tkinter.Canvas(container2)


def setLeftContainer():
	global label, entryLabel, searchEntry, fieldLabel, w
	label = Label(container, text="Search for a Patient\n")
	label.config(font=("Calibri", 14))
	entryLabel = Label(canvas1, text="Enter Search Criteria Here")
	searchEntry = tkinter.Entry(canvas1)
	canvas1.create_window(200, 140, window = searchEntry)
	fieldLabel = Label(canvas1, text="Select a field to search from")
	toSearch = searchEntry.get()
	w = OptionMenu(canvas1, variable, *OPTIONS)

def setRightContainer():
	global label1, sortLabel, v
	label1 = Label(container2, text="Sort Patient List\n")
	label1.config(font=("Calibri", 14))
	sortLabel = Label(canvas2, text="Choose from the Sorting Options")
	v = OptionMenu(canvas2, variable2, *SORTOPTIONS)

#function used for voice recognition if voice button is processed, handles which values to change in the gui
def setVarsAgain():
	print("Say 'sort by' or 'search by'")
	sortOrSearch = get_commands_from_mic.get_commands()
	if(sortOrSearch == 1):
		setDropDownVars(get_commands_from_mic.searchAndFilter(), 0)
		searchEntry.insert(0, get_commands_from_mic.getSearchCriteria())
		submit()
	elif(sortOrSearch == 2):
		setDropDownVars(0, get_commands_from_mic.sortBy())
		sortSubmit()

def pack():
	global button, button1
	left.pack(side="left", expand=True, fill="both")
	right.pack(side="right", expand=True, fill="both")
	container.pack(expand=True, fill="both", padx=5, pady=5)
	container2.pack(expand=True, fill="both", padx=5, pady=5)
	tableContainer.pack(expand=True, fill="both", padx=5, pady=5)
	tableContainer1.pack(expand=True, fill="both", padx=5, pady=5)
	button = Button(canvas1, text="Submit", command=submit)
	button1 = Button(canvas2, text="Sort", command=sortSubmit)

	label.pack(side="top")
	label1.pack(side="top")
	fieldLabel.grid(row=1, column=1)
	w.grid(row=1, column=2)
	entryLabel.grid(row=2, column=1)
	searchEntry.grid(row=2, column=2)
	button.grid(row=3, column=2)
	sortLabel.grid(row=1, column=1)
	v.grid(row=1, column=2)
	button1.grid(row=2, column=2)


	canvas1.pack()
	canvas2.pack()

def searchTable():
	global tv
	tv = ttk.Treeview(tableContainer, columns=(1,2,3), show="headings", height="20")
	tv.pack()
	tv.heading(1, text="UUID")
	tv.heading(2, text="Name")
	tv.heading(3, text="DOB")

def sortTable():
	global tv1
	tv1 = ttk.Treeview(tableContainer1, columns=(1,2,3), show="headings", height="20")
	tv1.pack()
	tv1.heading(1, text="UUID")
	tv1.heading(2, text="Name")
	tv1.heading(3, text="DOB")

#get columns from controller and display on the gui table
def onSubmit():
	tv.delete(*tv.get_children()) #clear table before new search
	for i in range(len(controller.column1)):
		tv.insert('', 'end', values=(controller.column1[i], controller.column2[i], controller.column3[i]))

def onSortSubmit():
	tv1.delete(*tv1.get_children())
	for i in range(len(controller.column11)):
		tv1.insert('', 'end', values=(controller.column11[i], controller.column12[i], controller.column13[i]))

def main():
	setWindow()
	setDropDownVars(0,0)
	setContainers()
	setLeftContainer()
	setRightContainer()
	pack()
	searchTable()
	sortTable()
	app.mainloop()

if __name__ == '__main__':
	main()
