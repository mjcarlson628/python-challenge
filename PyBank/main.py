# Main PyBank script
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    month_count = 0
    net_total = 0
    greatest_increase = 0
    increase_month = ""
    greatest_decrease = 0
    decrease_month = ""
    
    for row in csvreader:
        #print(row)
        month_count += 1
        net_total += int(row[1])

        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            increase_month = row[0]
        elif int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            decrease_month = row[0]
    
    print("Financial Analysis")
    print("------------------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${round(float(net_total/month_count), ndigits=2)}")
    print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")
         