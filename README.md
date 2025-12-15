This is a Python program to create case files. The case files have the following format.

MAIN DIRECTORY - CaseNumber_CaseAgent
  * Files: case_creation_log.txt, MAINDIRECTORY.docx
  * SUB DIRs - Line items
    * SUB DIRs - /img, /report, /exam_photos

  To compile to executable, use pyinstall. To install pyinstall: pip install pyinstaller
    * pyinstall --noconsole  --onefile caseCreator_v1.0.py

Profile functionality
* Currently, one profile is supported.
* The profile is serialized via Pickle and stored in the file profile.pr
* This file is NOT signed...yet

Known issues:
  * CyberTip toggle does not create the directories properly
  * Profile laods with out last name

TODO:
  * Add verbosity to log file
  * Fix CyberTip toggle
  * Allow for multiple entries in same instance
  * Allow adding images and legal documents
  * Make GUI prettier?
