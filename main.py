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

data = {}

with open('data.json', 'r') as fp:
    # data = pickle.load(fp)
    data = json.load(fp)
    
print()

result = solution(sys.argv[1], list(data.keys()))
# print("result", result)
for eachItem in result:
    print( eachItem, data[eachItem])