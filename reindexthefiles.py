from Files import *
import time

start_time = time.time()*100
multiprocessingIndexWordsAndFiles()
end_time = time.time()*100

total_time = end_time - start_time
print("Time requred to index=", total_time)