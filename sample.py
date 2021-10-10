import pickle
import json
import os
from multiprocessing import Process, Pool
import time
import asyncio

def readFromFiles( eachFile):
    data = {}
    
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
        
        # data += contentFromFile
        
    return contentFromFile
    '''with open('data.json', 'w') as fp:
        # pickle.dump(data, fp)
        json.dump(data, fp, indent=4)
        '''
    

def multiprocessingIndexWordsAndFiles():
    pool = Pool()
    
    fileList = []
    for eachFile in os.listdir():
        if eachFile.endswith(".txt"):
            fileList.append( eachFile)
    
    result_async = [pool.apply_async(readFromFiles, args = (x, )) for x in fileList]
    results = [r.get() for r in result_async]
    
    pool = Pool()
    pool = Pool(processes=len(os.listdir()))
    data = {}
    
    with open('data.json', 'w') as fp:
        # pickle.dump(data, fp)
        for contentFromFile in results:
            for key, value in contentFromFile.items():
                if data.get(key, None):
                    data[key]["File"].update( contentFromFile[key]["File"])
                else:
                    data[key] = contentFromFile[key]
        
        json.dump(data, fp, indent=4)
        
    print("Indexed")