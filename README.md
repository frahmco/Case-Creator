This is a Python program to create case files. The case files have the following format.

MAIN DIRECTORY - CaseNumber_CaseAgent
  Files: case_creation_log.txt, MAINDIRECTORY.docx
  SUB DIRs - Line items
    SUB DIRs - /img, /report, /exam_photos

  To compile to executable, use pyinstall. To install pyinstall: pip install pyinstaller
    pyinstall --noconsole caseCreator_v1.0.py


Known issues:
  CyberTip toggle does not create the directories properly

TODO:
  Add verbosity to log file
  Fix CyberTip toggle
  Allow for multiple entries in same instance
  Make GUI prettier?
