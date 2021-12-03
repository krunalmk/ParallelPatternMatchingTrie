# ParallelPatternMatchingTrie ( TriePDC)
## About the project
This project is Parallel and Distributed Computing course's J-component ( at VIT Chennai). Here main idea is to match and search words efficiently among text files in a directory. The files are indexed using multiprocessing. The indexed files are then searched using a Trie.
In other words, this project is word autocomplete using multiprocessing and trie.

## Report on the project
[Click here](https://github.com/krunalmk/TriePDC/blob/main/TriePDC:ParallelTextPatternMatching_Krunal.pdf) to read the report.

## Downloading the file
1. Execute following command to download the project.
```
git clone https://github.com/krunalmk/TriePDC.git
```
2. Extract the zip.

## Executing the project
1. Open terminal in the extracted folder.
2. Execute following
- for indexing the text files execute 
```
python3 reindexthefiles.py
```
- to get parallel prefix match for your input execute
```
python3 main.py <your word>
python3 main.py guten #Example: to get autocomplete suggestions from the text files for the word "guten".
```
## Algorithm used in project
### Algorithm for storing indexed data in JSON
1. The texts from text files in the current directory are read. 
2. Characters like '.', '\'', ',', ';', etc. are removed.
3. The cleaned text from step 2 is stored in JSON format in a file. The structure of the JSON ( data.json) is as follows:
```
{ word: {
        "File": {
                "filename1.txt": {
                                "Line": [ i1, i2, i3, ..., in]
                                },

                "filename2.txt": {
                                "Line": [ j1, j2, j3, ..., jn]
                                },
                }
        }
}
4. Multiprocessing concept is used to index the files efficiently.
                                    
```
### Algorithm for searching the prefix
1. The data from JSON ( data.json) is read and stored in Trie.
2. The Trie eases the process of searching. It is very efficient. For more information on Trie, [click here](https://en.wikipedia.org/wiki/Trie)
3. Now the query prefix ( entered by user in terminal/ console) is matched in the Trie. 
4. If match is found then file name along with line numbers of word is returned. You have got the results! Yayy!
