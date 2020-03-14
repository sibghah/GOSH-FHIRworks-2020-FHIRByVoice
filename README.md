FHIRByVoice

The application follows the Model-View-Controller approach

To run the app:
-on a terminal, locate to the directory in which gui.py is
-run python gui.py

To use the app:
-You can use the app by just searching or sorting the data through the GUI
-To use the voice, click on the "Voice" button
-The terminal will display prompts on what to say
-Wait for the microphone icon to appear on your system tray before saying whether you would like to search the data or sort it
	-Say "sort by" or "search by"
-Wait for the next terminal prompt and depending on the previous option say your next choice
	-if you are searching, choose a field from searchOptions* and say it, when the next terminal prompt appears say the search criteria
	-if you are sorting, choose a field from sortOptions** and say it 
-It's a good idea to wait for the microphone icon to appear on your system tray, since this will tell you exactly when the app is detecting your speech; when attempting to display this information on the GUI, it was too slow to work



Possible Further Developments:
-GUI displays prompts at the same time that the speech is being detected
-Using a chatbot along with the speech recognition for a better user experience, e.g. "I want a record of all patients born in 1965", instead of going through steps and saying specific things to diaplay the data

*searchOptions: "id", "name", "telecoms", "gender", "birth date", "addresses", "marital status", "multiple birth", "communications", "extensions", "identifiers"

**sortOptions: 
"alphabetical": to display data in an alphabetical order of full name, 
"oldest first": to display patient data sorted by age; oldest to youngest
"youngest first": to display patient data sorted by age: youngest to oldest

*Note: the prompts are not currently displayed on the GUI, since using Tkinter to update an entry was crashing the application
