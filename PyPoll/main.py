# Main PyPoll script
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join("Analysis", "PyPoll_analysis.txt")


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

    with open(output_path, "w") as outfile:
        outfile.write("Election Results\n")
        outfile.write("-------------------------------\n")
        outfile.write(f"Total Votes: {total_votes}\n")
        outfile.write("-------------------------------\n")
        
        for x in candidates:
    # print the percentage and total number of votes won by each candidate
    # display the percent to 3 decimals
            percent_won = results[x] * 100 / total_votes
            outfile.write(f"{x}: {format(percent_won, '.3f')}%  ({results[x]})\n")

    # find which key in the results dictionary has the highest value and declare the winner
        outfile.write("-------------------------------\n")
        outfile.write(f"Winner: {max(results, key = results.get)}\n")
        outfile.write("-------------------------------")
    
    print(open(output_path, "r").read())