from fhir_parser import FHIR
from fhir_parser.patient import Patient, Name, Telecom, Communications, Extension, Identifier
from datetime import date

fhir = FHIR()
patients = fhir.get_all_patients()

#switch statement used by controller to return the requested function to sort the data
def switch(choice):
	switcher={
		"Patient Names(A-Z)": sortAlphabeticalNames,
		"Age: Oldest to Youngest": sortOldesttoYoungest,
		"Age: Youngest to Oldest": sortYoungesttoOldest
	}
	func = switcher.get(choice)
	return func()

def sortAlphabeticalNames():
	ls = sorted(patients, key=lambda x:x.name.full_name, reverse=False)
	idList = []
	for i in range(len(ls)):
		idList.append(ls[i].uuid)
	return idList

def calculateAge(date):
	today = date.today()
	age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
	return age

def sortYoungesttoOldest():
	ls = sorted(patients, key=lambda x: calculateAge(x.birth_date), reverse=False)
	idList = []
	for i in range(len(ls)):
		idList.append(ls[i].uuid)
	return idList

def sortOldesttoYoungest():
	toReverse = sortYoungesttoOldest()
	toReverse.reverse()
	return toReverse
