from pathlib import Path
import csv
import os

# Define the path to the CSV file
csvpath = Path(r"C:\Users\JamesDavidson\Desktop\Challenge_Homeworks\Challenge2\python-homework\PyBank\Resources\budget_data.csv")

# Initialize variables to store financial metrics
total_months = 0
net_profit_loss = 0
average_change = 0
greatest_increase_date = ""
greatest_increase_amount = 0
greatest_decrease_date = ""
greatest_decrease_amount = 0

# Create empty lists to store the changes in profit/loss
profit_losses = []
dates = []


# Open the input path as a file object
with open(csvpath, 'r') as csvfile:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    budget_data = csv.reader(csvfile, delimiter=",")
    print(type(budget_data))
    
    # Skip the header row
    header = next(budget_data)

    # Loop through each row in the CSV file
    for row in budget_data:
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total months and net profit/loss
        total_months += 1
        net_profit_loss += profit_loss

        # Store profit/loss and date for calculating changes
        profit_losses.append(profit_loss)
        dates.append(date)

   

 # Calculate average change
for i in range(1, total_months):
    change = profit_losses[i] - profit_losses[i-1]
    average_change += change

    # Track greatest increase and decrease
    if change > greatest_increase_amount:
        greatest_increase_amount = change
        greatest_increase_date = dates[i]
    elif change < greatest_decrease_amount:
        greatest_decrease_amount = change
        greatest_decrease_date = dates[i]
        
# Calculate the average change
average_change /= (total_months - 1)

# Print the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Losses: {greatest_decrease_date} (${greatest_decrease_amount})")