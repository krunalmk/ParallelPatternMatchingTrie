import glob
import os
import re
import time
import csv

Queries = ["house", "proclaim", "hid", "father", "jump"]

# field names 
fields = ['Word', 'Time ( in milliseconds)']

filename = "bruteforce.csv"
        
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(fields) 
    
    for eachWord in Queries:
        start_time = time.time() * 1000
        print("----------------------------------\n\nKeyword =", eachWord)
        for filename in glob.glob('*.txt'):
            with open(os.path.join(os.getcwd(), filename), 'r') as f:
                text = f.read()
                print("In", filename, "-\n")
                result = [_.start() for _ in re.finditer(eachWord, text)] 
                print(result)
            print()
        end_time = time.time() * 1000
        total_time = end_time - start_time
        csvwriter.writerow([eachWord, total_time]) 
