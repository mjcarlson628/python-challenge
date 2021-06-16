# Main PyBank script
# Analysis of budget_data.csv
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
# read budget_data.csv
    csvreader = csv.reader(csvfile, delimiter=',')
# store the header row
    csv_header = next(csvreader)

# create variables to count the number of months and total money
    month_count = 0
    net_total = 0

# set the values to beat for greatest increase/decrease to 0
    greatest_increase = 0
    increase_month = ""
    greatest_decrease = 0
    decrease_month = ""
    
    for row in csvreader:
# loop through all months
# increase the number of months and update the net profit/loss
        month_count += 1
        net_total += int(row[1])

# compare profit/loss to the current greatest value
# store the month when there is a change in greatest increase/decrease
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            increase_month = row[0]
        elif int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            decrease_month = row[0]
    
# print the number of months, net total, average monthly change,
# and months with the greatest profit and loss
    print("Financial Analysis")
    print("------------------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${round(float(net_total/month_count), ndigits=2)}")
    print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")
         