import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#Set the veriables to store the data
total_Votes = 0 
candidate_dictionary= {}
max_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    
    #Skip Header
    next(csvreader)

    for row in csvreader:
    #The total number of votes cast
        total_Votes += 1
        name = row[2]

    #A complete list of candidates who received votes
        if name not in candidate_dictionary:
            candidate_dictionary[name] = 0
            
        candidate_dictionary[name] += 1 


    print(f"Election Results")
    print(f"--------------------")
    print(f"{total_Votes}")
    print(f"--------------------")

    for name, votes in candidate_dictionary.items():
    #The percentage of votes each candidate won
        percentage = round(votes / total_Votes * 100, 2)
        print(f"{name}: {percentage}% ({votes})")

    #The winner of the election based on popular vote
        if votes > max_votes:
            max_votes = votes
            winner = name 


print(f"--------------------")   
print(f"The winner is {winner}!")
print(f"--------------------") 

#write to a text file in the "analysis" directory

output_dir = 'analysis'
output_path = os.path.join(output_dir, 'Results.txt')

with open(output_path, "w") as outfile:
    outfile.write(f"Election Results")
    outfile.write(f"--------------------")
    outfile.write(f"{total_Votes}")
    outfile.write(f"--------------------")

    for name, votes in candidate_dictionary.items():
        percentage = round(votes / total_Votes * 100, 2)
        outfile.write(f"{name}: {percentage}% ({votes})\n")

    outfile.write(f"--------------------")
    outfile.write(f"The winner is {winner}!")
    outfile.write(f"--------------------")