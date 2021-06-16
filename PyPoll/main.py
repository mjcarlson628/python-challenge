# Main PyPoll script
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_votes = 0
    candidates = []
    results = {}

    for row in csvreader:
        total_votes += 1
        #print(total_votes)
        if row[2] not in candidates:
            candidates.append(row[2])
            results[row[2]] = 1
        else:
            results[row[2]] += 1

    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------------")
    
    for x in candidates:
        percent_won = results[x] * 100 / total_votes
        print(f"{x}: {format(percent_won, '.3f')}%  ({results[x]})")
 
    print("-------------------------------")
    print(f"Winner: {max(results, key = results.get)}")
    print("-------------------------------")