import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Set variables to store data
totalMonths = 0
net = 0
profitChanges = []
months = []

# Open the CSV file and read it
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the Header
    next(csvreader)

    # Loop through each row
    for row in csvreader:

        # Increment the total number of months and net profit
        totalMonths += 1
        net += int(row[1])

        # Store the month and profit data
        months.append(row[0])
        profitChanges.append(int(row[1]))

    # Calculate the changes in profit/loss over the entire period
    changeInprofit = []
    for x in range(1, len(profitChanges)):
        changeInprofit.append(profitChanges[x] - profitChanges[x-1])

    # Calculate the average change in profit/loss over the entire period
    average_changeInprofit = sum(changeInprofit) / len(changeInprofit)

    # Find the greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(changeInprofit)
    greatest_increase_date = months[changeInprofit.index(greatest_increase) + 1]

    # Find the greatest decrease in profits (date and amount) over the entire period
    greatest_decrease = min(changeInprofit)
    greatest_decrease_date = months[changeInprofit.index(greatest_decrease) + 1]

# Print the financial analysis results
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${net}")
print(f"Average Change: ${round(average_changeInprofit, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

output_dir = 'analysis'
output_path = os.path.join(output_dir, 'Results.txt')

with open(output_path, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write(f"--------------------\n")
    outfile.write(f"Total Months: {totalMonths}\n")
    outfile.write(f"Total: ${net}\n")
    outfile.write(f"Average Change: ${round(average_changeInprofit, 2)}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
