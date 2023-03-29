import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    #Skip Header
    next(csvreader)

    # Initialize variables
    total_votes = 0
    candidates = {}
   
    for row in cvsfile:
        # Count the total number of votes
        total_votes += 1

        # Check if the candidate already exists in the dictionary
        if row[2] not in candidates:
            candidates[row[2]] = 0

        # Count the votes for each candidate
        candidates[row[2]] += 1

# Calculate the percentage of votes for each candidate and find the winner
winner = ""
max_votes = 0
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")