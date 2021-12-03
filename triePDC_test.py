import sys
import time
from Trie import *
from Files import *
import csv

def solution(searchPrefix, listOfStreamers):
    status = [["Found"], ["noMatches"]]
    t = Trie() 
    t.formTrie(listOfStreamers)
    comp = t.printAutoSuggestions(searchPrefix) 

    if len(comp) <= 0: 
        return(status[1])
    else:
        return comp

def getSearchResults( TheTrie, searchPrefix):
    status = [["Found"], ["noMatches"]]
    comp = TheTrie.printAutoSuggestions( searchPrefix)
    
    if len(comp) <= 0: 
        return(status[1])
    else:
        return comp

data = {}

with open('data.json', 'r') as fp:
    # data = pickle.load(fp)
    data = json.load(fp)
    
print()

start_time = time.time() * 1000
TheTrie = Trie()
TheTrie.formTrie(data.keys())
end_time = time.time() * 1000
time_to_create_trie = end_time-start_time
print("Time required for creating Trie from indexed file is", time_to_create_trie, "ms")

# field names 
fields = ['Word', 'Time ( in milliseconds)']


Queries = ["house", "proclaim", "hid", "father", "jump"]
# writing the fields 
filename = "analysis.csv"
        
    # writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    
    # writing the fields 
    csvwriter.writerow(fields) 
    
    for eachWord in Queries:
        
        start_time = time.time() * 1000
        result = getSearchResults( TheTrie, eachWord)
        # print("result", result)
        for eachItem in result:
            print(end='')

        end_time = time.time() * 1000
        total_time = end_time-start_time
        print("Time required for execution is", total_time, "ms")
        
        csvwriter.writerow([eachWord, total_time]) 