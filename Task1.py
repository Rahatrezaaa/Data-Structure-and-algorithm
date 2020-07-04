"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#creating an empty list to store all telephone numbers
numbers=[]

#appending all numbers of calls dataset to the list
for row in calls:
    numbers.append(row[0])    #phone number of sender
    numbers.append(row[1])    #phone number of receiver
    
#appending all numbers of texts dataset to the list
for row in texts:
  numbers.append(row[0])    #phone number of sender
  numbers.append(row[1])    #phone number of receiver

#using set data structure to find unique numbers

print("There are {} different telephone numbers in the records.".format(len(set(numbers))))