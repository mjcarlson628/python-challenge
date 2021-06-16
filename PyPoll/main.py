# Main PyPoll script
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
# read election_data.csv
    csvreader = csv.reader(csvfile, delimiter=',')
# store the header row
    csv_header = next(csvreader)

# running total number of votes
    total_votes = 0
# list of candidate names
    candidates = []
# dictionary to store each candidate's name with the votes for that person
    results = {}

    for row in csvreader:
# loop through all rows and increase total vote count each time
        total_votes += 1

# check to see if a name has already been added to the candidates list
        if row[2] not in candidates:
# add the name to the list if it's not already there
            candidates.append(row[2])
# save the name to the results dictionary and count it as their first vote
            results[row[2]] = 1
        else:
# if the name has been encountered, count it as one more vote in results
            results[row[2]] += 1

    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------------")
    
    for x in candidates:
# print the percentage and total number of votes won by each candidate
# display the percent to 3 decimals
        percent_won = results[x] * 100 / total_votes
        print(f"{x}: {format(percent_won, '.3f')}%  ({results[x]})")

# find which key in the results dictionary has the highest value and declare the winner
    print("-------------------------------")
    print(f"Winner: {max(results, key = results.get)}")
    print("-------------------------------")