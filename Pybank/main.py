# Modules
import os
import csv

print("Financial Analysis")
print("-------------------------")

# Set path for file
csvpath = r"Pybank/Resources/budget_data.csv"
# csvpath = os.path.join("..","Resources", "budget_data.csv")

column_index_0 = 0
column_index_1 = 1

# Initialize variables to store the max increase/decrease and corresponding date
greatest_increase = 0
previous_value = None
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #The total number of months
    mo_yr = [row[column_index_0] for row in csvreader]
    print("Total Months: " + str(len(mo_yr)))
#-----------------------------------------------#

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

 #inital the total P&L variable
    total_PL = 0
    for row in csvreader:
        try:
            total_PL = total_PL + int(row[column_index_1])
        except ValueError:
            pass # Skip non-numeric values
    print("Total: $" + str(total_PL))
#-----------------------------------------------#        

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")   
    PL = [row[column_index_1] for row in csvreader]
    average_change = round((int(PL[(len(PL)-1)]) - int(PL[0]))/(len(PL)-1),2)
    print("Average Change: $" + str(average_change))
#-----------------------------------------------------#


    #The greatest increase in profits (date and amount) over the entire period

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Iterate through the remaining rows
    for row in csvreader:

        # Assign the current value
        current_value = int(row[1])
        
            # Calculate max increase/decrease and date if not the first row
        if previous_value is not None:
            increase = current_value - previous_value
            decrease = current_value - previous_value
            if increase > greatest_increase:
                greatest_increase = increase
                greatest_increase_date = row[0]
            if decrease < greatest_decrease:
                greatest_decrease = decrease
                greatest_decrease_date = row[0]

        # Update previous value for the next iteration
        previous_value = current_value
print("Greatest Increase in profits: " + str(greatest_increase_date + " ($" + str(greatest_increase) + ")"))
print("Greatest Decrease in profits: " + str(greatest_decrease_date + " ($" + str(greatest_decrease) + ")"))

#------------------------------
# Pybank results
pybank_results = {
    "Total Months": "86",
    "Total": "$22564198",
    "Average Change": "$-8311.11",
    "Greatest Increase in profits": "Aug-16 ($1862002)",
    "Greatest Decrease in profits": "Feb-14 ($-1825558)"
}

# Export results to text file
with open("Pybank Financial Analysis.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------\n")
    for key, value in pybank_results.items():
        file.write(f"{key}: {value}\n")
    file.write("\n")






    

