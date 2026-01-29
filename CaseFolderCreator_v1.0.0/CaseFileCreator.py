import os
from docx import Document as Doc
import datetime 

#Class for Case File Creator
class CaseFileCreator:


    def __init__(self):
        pass        

    #Method to create directories, subdirectories, and Word Doc for report
    def createDirectories(self, caseNumber, caseAgent, items, filePath):
        current_time = datetime.datetime.now()
        

        paths = []
        subDirs = ['img', 'report', 'exam_photos']
        topDir = filePath + '/' + (caseNumber + '_' + caseAgent)

        #Make the top level directory as CASENUMBER_AGENT
        try:
            os.mkdir(topDir)
            log_file = open(topDir + '/' + "case_creation_log.txt", "w")
            print (f"Directory '{topDir}' created succesfully")
            log_file.write(f"Directory '{topDir}' created succesfully \n")
        except FileExistsError:
            print(f"DIRECTORY '{topDir}' ALREADY EXISTS")
        except PermissionError:
            print(f"PERMISSION DENIED")
        except Exception as e:
            print(f"An error occured: {e}")

        #Create Log File
    

        log_file.write("Case Number: " + caseNumber + '\n')
        log_file.write("Case Agent/Detective: " + caseAgent + '\n')
        log_file.write("Case Generated on: " + current_time.strftime("%c") + '\n\n\n')
        log_file.write("Program Logs\n--------------------\n") 
        log_file.write(f"Directory '{topDir}' created succesfully\n")

        #Create word doc for report, same name as top level directory
        report_doc = Doc()
        report_doc.save(topDir + '/' + caseNumber + '_' + caseAgent + '.docx')

        #Create item folders and store them
        for item in items:
            paths.append(topDir + '/' + item)

        #Generate item folders
        for path in paths:
            try:
                os.mkdir(path)
                log_file.write(f"Directory '{path}' created succesfully \n")
            except FileExistsError:
                log_file.write(f"DIRECTORY '{topDir}' ALREADY EXISTS")
            except PermissionError:
                log_file.write(f"PERMISSION DENIED")
            except Exception as e:
                log_file(f"An error occured: {e}")

        #Generate item subfolders
        for path in paths:
            print(path)
            for j in range (0, len(subDirs)):
                t = path + '/' + subDirs[j]
                try:
                    os.mkdir(t)
                    log_file.write(f"Directory '{t}' created succesfully\n")
                except FileExistsError:
                    log_file.write(f"DIRECTORY '{t}' ALREADY EXISTS")
                except PermissionError:
                    log_file.write(f"PERMISSION DENIED")
                except Exception as e:
                    log_file.write(f"An error occured: {e}")

        log_file.close()


    #EXPERIMENTAL Creates Direcotries for CT Triage    
    def createCybertipDirectories(self, tipNumber, electronicServiceProvider, filePath):
        topDir = filePath + tipNumber +' (' + electronicServiceProvider + ')'
        firstLevelSubDirs = ["cyber tip", "intel", "legal"]
        tipSubDirs = ["CSAM"]
        legalSubDirs = ["SDT", "SW"]
        

        try:
            os.mkdir(topDir)
        except FileExistsError:
            print(f"DIRECTORY '{topDir}' ALREADY EXISTS")
        except PermissionError:
            print(f"PERMISSION DENIED")
        except Exception as e:
            print(f"An error occured: {e}")
        
        for dir in firstLevelSubDirs:
            tempDir = topDir + '/' + dir
            if dir == "cyber tip":
                try:
                    os.mkdir(tempDir)
                    for sd in tipSubDirs:
                        tempDir = topDir + '/' + dir
                        tempDir = tempDir + '/' + sd
                        os.mkdir(tempDir)
                except FileExistsError:
                    print(f"DIRECTORY '{tempDir}' ALREADY EXISTS")
                except PermissionError:
                    print(f"PERMISSION DENIED")
                except Exception as e:
                    print(f"An error occured: {e}")
            
            if dir == "legal":
                try:
                    os.mkdir(tempDir)
                    for sd in legalSubDirs:
                        tempDir = topDir + '/' + dir
                        tempDir = tempDir + '/' + sd
                        os.mkdir(tempDir)
                except FileExistsError:
                    print(f"DIRECTORY '{tempDir}' ALREADY EXISTS")
                except PermissionError:
                    print(f"PERMISSION DENIED")
                except Exception as e:
                    print(f"An error occured: {e}")
            
            elif dir == "intel":
                try:
                    os.mkdir(tempDir)
                except FileExistsError:
                    print(f"DIRECTORY '{tempDir}' ALREADY EXISTS")
                except PermissionError:
                    print(f"PERMISSION DENIED")
                except Exception as e:
                    print(f"An error occured: {e}")

        report_doc = Doc()
        report_doc.save(topDir + '/' + "MASTER_Notes.docx")


                

        
        
        
        
        
