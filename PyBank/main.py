# Main PyBank script
# Analysis of budget_data.csv
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
output_path = os.path.join("Analysis", "PyBank_analysis.txt")

with open(csvpath) as csvfile:
# read budget_data.csv
    csvreader = csv.reader(csvfile, delimiter=',')
# store the header row
    csv_header = next(csvreader)

# create variables to count the number of months and total money
    month_count = 0
    net_total = 0

    previous_profit = 0
    current_profit = 0
    profit_change = 0
    total_change = 0

# set the values to beat for greatest increase/decrease to 0
    greatest_increase = 0
    increase_month = ""
    greatest_decrease = 0
    decrease_month = ""
    
    for row in csvreader:
# loop through all months
# increase the number of months and update the net profit/loss
        month_count += 1
        current_profit = int(row[1])
        net_total += current_profit

# compare each month's profit to the previous month
        if month_count > 1:
            profit_change = current_profit - previous_profit
            total_change += profit_change

# compare profit/loss to the current greatest value
# store the month when there is a change in greatest increase/decrease
        if profit_change > greatest_increase:
            greatest_increase = profit_change
            increase_month = row[0]
        elif profit_change < greatest_decrease:
            greatest_decrease = profit_change
            decrease_month = row[0]

        previous_profit = int(row[1])

    with open(output_path, "w") as outfile:
# write the number of months, net total, average monthly change,
# and months with the greatest profit and loss to a text file
        outfile.write("Financial Analysis\n")
        outfile.write("------------------------------------\n")
        outfile.write(f"Total Months: {month_count}\n")
        outfile.write(f"Total: ${net_total}\n")
        outfile.write(f"Average Change: ${round(float(total_change/(month_count - 1)), ndigits=2)}\n")
        outfile.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
        outfile.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# print the results to the terminal
    print(open(output_path, "r").read())           