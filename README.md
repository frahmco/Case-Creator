This is a Python program to create case files. The case files have the following format.

MAIN DIRECTORY - CaseNumber_CaseAgent
  * Files: case_creation_log.txt, MAINDIRECTORY.docx
  * SUB DIRs - Line items
    * SUB DIRs - /img, /report, /exam_photos

  To compile to executable, use pyinstall. To install pyinstall: pip install pyinstaller
    * pyinstall --noconsole  --onefile caseCreator_v[VERSION].py

Profile functionality PROFILE FUNCTIONALITY IS NOT AVAILABLE IN v2.0.0
* Currently, one profile is supported.
* The profile is serialized via Pickle and stored in the file profile.pr
* This file is NOT signed...yet

Known issues:
  * CyberTip toggle does not create the directories properly
  * Issue error handling when fields left blank

VERSION 2.0.0 UPDATE
------------------------
* Completely refactored code base
* Added attachment capabilities w/ hashing
* Better error handling
* More verbose logs

TODO:
* Make ThreadPool for hashing function
* Make GUI more friendly
* Fix error handling issues
* Restore profile functionality
