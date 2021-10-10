import pickle
import json
import os
import multiprocessing
import time

def readFromFiles():
    data = {}
    for eachFile in os.listdir():
        if eachFile.endswith(".txt"):
            with open(eachFile) as file:
                contentFromFile = {}
                i = 0
                page = 0
                temp = " "
                while page != 2000:
                    temp = file.readline().strip()
                    wordInfo = temp.strip().split()
                    
                    for each in range (len( wordInfo)):
                        
                        wordInfo[each] = wordInfo[each].replace(".", "") #wordInfo[each] = 
                        wordInfo[each] = wordInfo[each].replace("*", "") #wordInfo[each] = 
                        wordInfo[each] = wordInfo[each].replace(",", "") #wordInfo[each] = 
                        wordInfo[each] = wordInfo[each].replace("!", "") #wordInfo[each] = 
                        wordInfo[each] = wordInfo[each].replace("    ", "") #wordInfo[each] = 
                        wordInfo[each] = wordInfo[each].replace(";", "") #wordInfo[each] = 
                        wordInfo[each] = wordInfo[each].replace(":", "") #wordInfo[each] = 
                        wordInfo[each] = wordInfo[each].replace("?", "") #wordInfo[each] = 
                        #wordInfo[each] = wordInfo[each].replace("", "") #wordInfo[each] = 
                        wordInfo[each] = wordInfo[each].lower()
                        
                        # print(eachFile, wordInfo[each])
                        
                        if wordInfo[each] not in contentFromFile:
                            contentFromFile[wordInfo[each]] = {"File": {eachFile: {"Line":[i]}}}
                        else:
                            contentFromFile[wordInfo[each]]["File"][eachFile]["Line"].append(i)
                    i += 1
                    page += 1
                for key, value in contentFromFile.items():
                    if data.get(key, None):
                        data[key]["File"].update( contentFromFile[key]["File"])
                    else:
                        data[key] = contentFromFile[key]
                # data += contentFromFile
    
    with open('data.json', 'w') as fp:
        # pickle.dump(data, fp)
        json.dump(data, fp, indent=4)