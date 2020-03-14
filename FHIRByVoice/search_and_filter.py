from fhir_parser import FHIR
from fhir_parser.patient import Patient, Name, Telecom, Communications, Extension, Identifier

searchF = None
searchC = None
patients = None

#function used by the gui class to set the data that is being searched for
def setVariables(searchField, searchCriteria):
	searchF= searchField
	searchC = searchCriteria
	fhir = FHIR()
	global patients
	patients = fhir.get_all_patients()

#functions used by switch statement to return matching data from required field

def searchUUID(c):
	ls = []
	for patient in patients:
		if(patient.uuid == c):
			ls.append(patient.uuid)
	return ls

def searchName(c):
	ls = []
	for patient in patients:
		if(patient.name.full_name == c):
			ls.append(patient.uuid)
	return ls

def searchTelecoms(c):
	ls = []
	for patient in patients:
		if(patient.telecoms == c):
			ls.append(patient.uuid)
	return ls

def searchGender(c):
	ls = []
	for patient in patients:
		if(patient.gender == c):
			ls.append(patient.uuid)
	return ls

def searchDOB(c):
	ls = []
	for patient in patients:
		if(patient.birth_date == c):
			ls.append(patient.uuid)
	return ls

def searchAddresses(c):
	ls = []
	for patient in patients:
		if(patient.addresses == c):
			ls.append(patient.uuid)		
	return ls

def searchmStatus(c):
	ls = []
	for patient in patients:
		if(patient.marital_status == c):
			ls.append(patient.uuid)
	return ls

def searchComms(c):
	ls = []
	for patient in patients:
		if(patient.communications == c):
			ls.append(patient.uuid)
	return ls

def searchExtensions(c):
	ls = []
	for patient in patients:
		if(patient.extensions == c):
			ls.append(patient.uuid)	
	return ls

def searchID(c):
	ls = []
	for patient in patients:
		if(patient.identifiers == c):
			ls.append(patient.uuid)
	return ls

#python style switch statement using dictionaries, used by the controller to return the required function
def switch(choice, c):
	switcher={
		"UUID": searchUUID,
		"Name": searchName,
		"Telecoms": searchTelecoms,
		"Gender": searchGender,
		"Birth Date": searchDOB,
		"Addresses": searchAddresses,
		"Marital Status": searchmStatus,
		"Communications": searchComms,
		"Extensions": searchExtensions,
		"Identifiers": searchID
	}
	func = switcher.get(choice)
	return func(c)
