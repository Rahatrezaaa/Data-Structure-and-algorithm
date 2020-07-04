"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
#creating empty dictionary for tracking of duration and numbers
dictionary={}    

#iterating over all rows of call dataset
for i in range(len(calls)):
  
    key_for_dialler=calls[i][0]    
    key_for_receiver=calls[i][1]   
    time_spent=int(calls[i][3])
    
    #I am going to make lists of dictionaries,where list will be of durations involving that particular phone number.
    
    #check if particular number is coming for first time or not
    if dictionary.get(key_for_dialler) is None:
        dictionary[key_for_dialler]=[time_spent] 
        
    elif dictionary.get(key_for_dialler) is not None:
        dictionary[key_for_dialler].append(time_spent)
    
    if dictionary.get(key_for_receiver) is None:
        dictionary[key_for_receiver]=[time_spent]
    elif dictionary.get(key_for_receiver) is not None:
        dictionary[key_for_receiver].append(time_spent)

#getting sum of the durations 
for number,time in dictionary.items():
    dictionary[number]=sum((time))


tele_number_with_maxtime=max(dictionary,key=dictionary.get)
max_time=dictionary[tele_number_with_maxtime]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(tele_number_with_maxtime,max_time))

    