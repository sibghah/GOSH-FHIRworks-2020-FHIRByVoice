from flask import Flask, jsonify
from flask_restful import Resource, Api
from fhir_parser import FHIR
import sort

#get functions that could be used by the FHIRByVoice app
#data is displayed in json format on port:8050
#must first run FHIR server before using this API

fhir = FHIR()
patients = fhir.get_all_patients()

app = Flask(__name__)
api = Api(app)

def getPatientName(id):
	for patient in patients:
		if(id == patient.uuid):
			return patient.name.full_name

def getPatientDOB(id):
	for patient in patients:
		if(id == patient.uuid):
			return patient.birth_date

@app.route("/api/PatientInfo", methods= ['GET'])
def getPatientInfo():
	jsonPatientInfo = []
	for patient in patients:
		jsonPatientInfo.append(({"patientID": patient.uuid, "patientFullName": patient.name.full_name, "patientDateOfBirth": patient.birth_date}))
	return jsonify({"PatientIDs": jsonPatientInfo})

@app.route("/api/PatientBirthDays", methods= ['GET'])
def getBirthDays():
	jsonBirthDays = []
	for patient in patients:
		jsonBirthDays.append({"birth_date": patient.birth_date})
	return jsonify({"PatientBirthDays": jsonBirthDays})

@app.route("/api/PatientIDs", methods=['GET'])
def getPatientIDs():
	jsonPatientIDs = []
	for patient in patients:
		jsonPatientIDs.append({"patient_ID": patient.uuid})
	return jsonify({"PatientIDs": jsonPatientIDs})

@app.route("/api/PatientFullNames", methods= ['GET'])
def getPatientNames():
	jsonFullNames = []
	for patient in patients:
		jsonFullNames.append({"patient_full_name": patient.name.full_name})
	return jsonify({"PatientFullNames": jsonFullNames})

@app.route("/api/sortedAlphabeticalNames", methods=['GET'])
def getPatientNamesSortedAlphabetically():
	listofIds = []
	sortedList = sort.sortAlphabeticalNames()
	for id in sortedList:
		listofIds.append({"patientID": id, "patientName": getPatientName(id)})
	return jsonify({"SortedPatientNamesAlphabetical" :listofIds})

@app.route("/api/sortedYoungesttoOldest", methods= ['GET'])
def getSortedYoungesttoOldest():
	listofIds = []
	sortedList = sort.sortYoungesttoOldest()
	for id in sortedList:
		listofIds.append({"patientID": id, "patientName": getPatientName(id), "patient_birth_date": getPatientDOB(id)})
	return jsonify({"SortedPatientsYoungesttoOldest" :listofIds})

@app.route("/api/sortedOldesttoYoungest", methods= ['GET'])
def getSortedOldesttoYoungest():
	listofIds = []
	sortedList = sort.sortOldesttoYoungest()
	for id in sortedList:
		listofIds.append({"patientID": id, "patientName": getPatientName(id), "patient_birth_date": getPatientDOB(id)})
	return jsonify({"SortedPatientsOldesttoYoungest" :listofIds})

if __name__ == '__main__':
	app.run(debug=True, port=8050)