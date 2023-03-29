import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#Set the veriables to store the data
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won

total_Votes = 0 
names = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip Header
    next(csvreader)

For row in csvfile
    total_Votes += 1

if row[2] not in names:
     



#The winner of the election based on popular vote

#Your analysis should align with the following results:
