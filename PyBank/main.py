import os

import csv

csvpath = os.path.join("Resources","budget_data.csv")

analysis = ("c:/Users/Allister Rebello/Desktop/Analysis Projects/Unit 03 - Python/Module 3/python-challenge/PyBank/analysis")

output_file_path = os.path.join("analysis", "Financial_Analysis.txt")

Total_Months = 0
Net_Total = 0
Previous_Profit_Loss = 0
Changes = []
Dates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)
   
    # Skip Header row
    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

        # Extract values from current row
        Date = row[0]
        Profit_Loss = int(row[1])

        # Calculate total number of months
        Total_Months += 1

        # Calculate net total amount of Profit/Losses
        Net_Total += Profit_Loss


        # Calculate change in Profit/Losses from previous month
        if Total_Months > 1:
            Change = Profit_Loss - Previous_Profit_Loss
            Changes.append(Change)
            Dates.append(Date)

        # Update the Previous Profit/Losses for next iteration
        Previous_Profit_Loss = Profit_Loss

    # Calculate the average change
    Average_Change = sum(Changes)/ len(Changes)

    # Calculate Greatest Increase and Decrease in Profits
    Greatest_Increase = max(Changes)
    Greatest_Increase_Date = Dates[Changes.index(Greatest_Increase) + 1]  

    Greatest_Decrease = min(Changes)
    Greatest_Decrease_Date = Dates[Changes.index(Greatest_Decrease) + 1]  

# Print the financial analysis results
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Net_Total}")
print(f"Average Change: ${round(Average_Change, 2)}")
print(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease})")

# Print & save the results to a text file
with open('Financial_Analysis.txt', "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-----------------------------\n")
    output_file.write(f"Total Months: {Total_Months}\n")
    output_file.write(f"Total: ${Net_Total}\n")
    output_file.write(f"Average Change: ${round(Average_Change, 2)}\n")
    output_file.write(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease})\n")
    



