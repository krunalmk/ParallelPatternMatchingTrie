import sys
import pickle
from Trie import *
from Files import *

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
    data = json.load(fp)
    
print()

TheTrie = Trie()
TheTrie.formTrie(data.keys())

result = getSearchResults( TheTrie, sys.argv[1])

# print("result", result)
for eachItem in result:
    print( eachItem, data[eachItem])