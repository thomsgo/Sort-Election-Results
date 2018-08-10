import os
import csv

from operator import itemgetter

# Initialize variables
total_votes = 0
total_candidates = 0
candidate_options = []
candidate_votes = {}

#open the csv file with the election results
with open("Election Data Sample.csv", newline="") as csvfile:
    # Create a dictionary with the data
    csvreader = csv.DictReader(csvfile, delimiter=",")
    # Cycle through rows in dictionary, find candidate names and sum their voting results
    for row in csvreader:
        total_votes = total_votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_options:
            # Create a new candidate if not already in list
            candidate_options.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 1    
        else:
            # Add next voting selection to candidates totals
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

            # Sort results based on most votes
winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

# Print results to screen
print(f'Election Results')
print(f'--------------------')
print(f'Total Votes: {total_votes}')
print(f'--------------------\n')
for candidate in candidate_votes:
    print(f'{candidate:<12}{str(round(((candidate_votes[candidate]/total_votes)*100)))}%  ({str(candidate_votes[candidate])})')
print(f'\n-----------------------------')
print(f'Election Winner: {str(winner[0][0])}')
print(f'-----------------------------')
# Print results to a text file
with open("Election Results.txt", "w") as text_file:
    print(f'Election Results', file=text_file)
    print(f'------------------', file=text_file)
    print(f'Total Votes: {total_votes}', file=text_file)
    print(f'------------------\n', file=text_file)
    for candidate in candidate_votes:
        print(f'{candidate:<12}{str(round(((candidate_votes[candidate]/total_votes)*100)))}%  ({str(candidate_votes[candidate])})', file=text_file)
    print(f'\n---------------------------', file=text_file)
    print(f'Election Winner: {str(winner[0][0])}', file=text_file)
    print(f'---------------------------', file=text_file)
# End
