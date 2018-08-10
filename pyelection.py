import os
import csv

from operator import itemgetter

total_votes = 0
total_candidates = 0
candidate_options = []
candidate_votes = {}

#open the csv file
with open("Election Data Sample.csv", newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    for row in csvreader:
        total_votes = total_votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_options:
            candidate_options.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 1    
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

print(f'Election Results')
print(f'--------------------')
print(f'Total Votes: {total_votes}')
print(f'--------------------\n')
for candidate in candidate_votes:
    print(f'{candidate:<12}{str(round(((candidate_votes[candidate]/total_votes)*100)))}%  ({str(candidate_votes[candidate])})')
print(f'\n-----------------------------')
print(f'Election Winner: {str(winner[0][0])}')
print(f'-----------------------------')

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
    