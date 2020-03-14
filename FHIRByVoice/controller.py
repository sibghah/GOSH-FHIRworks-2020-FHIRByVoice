from fhir_parser import FHIR
from fhir_parser.patient import Patient, Name, Telecom, Communications, Extension, Identifier
from search_and_filter import switch
import sort

fhir = FHIR()
patients = fhir.get_all_patients()
listofIDs = []
column1 = []
column2 = []
column3 = []

listofIDs1 =[]
column11 = []
column12 = []
column13 = []

#function to process user's selected search field and criteria
#columns that are being appended to will be used by the gui to show in table
def showSelection(choice, criteria):
	column1.clear() #clear columns before next search/sort
	column2.clear()
	column3.clear()
	listofIDs = switch(choice, criteria) #get ids to find the other patient info
	for i in range(len(listofIDs)):
		for patient in patients:
			if(patient.uuid==listofIDs[i]):
				column1.append(patient.uuid)
				column2.append(patient.name.full_name)
				column3.append(patient.birth_date)

#function to process user's selected sort by choice
def sortSelection(choice):
	column11.clear()
	column12.clear()
	column13.clear()
	listofIDs1 = sort.switch(choice)
	for i in range(len(listofIDs1)):
		for patient in patients:
			if(patient.uuid==listofIDs1[i]):
				column11.append(patient.uuid)
				column12.append(patient.name.full_name)
				column13.append(patient.birth_date)	


			