# Modules
import os
import csv

# Set path for file
csvpath = r"Pybank/Resources/budget_data.csv"
# csvpath = os.path.join("..","Resources", "budget_data.csv")

column_index_0 = 0
column_index_1 = 1
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header
       
    mo_yr = [row[column_index_0] for row in csvreader]
    print(len(mo_yr))

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

 #inital the total P&L variable
    total_PL = 0
    for row in csvreader:
        try:
            total_PL = total_PL + int(row[column_index_1])
        except ValueError:
            pass # Skip non-numeric values
    print(total_PL)

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")   
    PL = [row[column_index_1] for row in csvreader]
    average_change = round((int(PL[(len(PL)-1)]) - int(PL[0]))/(len(PL)-1),2)
    print(average_change)


    

