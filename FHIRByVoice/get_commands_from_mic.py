import time
import random 
import speech_recognition as sr

#user speech converted to numbers that can be used to set the variable for the drop downs
def convertOptions(searchField):
	#python switch statement using dictionaries
	switch={
		"i d":1,
		"name":2,
		"telecoms":3,
		"gender":4,
		"birth date":5,
		"addresses":6,
		"marital status":7,
		"multiple birth":8,
		"communications":9,
		"extensions":10,
		"identifiers":11
	}
	return switch.get(searchField)

def convertSortOptions(sortSelection):
	switch={
		"alphabetical":1,
		"oldest first":2,
		"youngest first":3
	}
	return switch.get(sortSelection)

#using python's speech_recognition library to return user speech as text
def detect_speech():
	r = sr.Recognizer()
	m = sr.Microphone()

	with m as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	return r.recognize_google(audio)

#does the user want to search or sort data?
def get_commands():
	command = detect_speech().lower()
	if(command == "search by"):
		return 1
	elif(command == "sort by"):
		return 2

#which field user wants to search 
#use switch statment to return drop down variable
def searchAndFilter():
	print("Say which field you would like to search")
	field = detect_speech().lower()
	return convertOptions(field)

#criteria that user will use to search data
def getSearchCriteria():
	print("Say the criteria for searching")
	criteria = detect_speech().lower()
	return criteria

#how does the user want to sort the data
def sortBy():
	print("Say how you would like to sort the data")
	sort_field = detect_speech().lower()
	return convertSortOptions(sort_field)
