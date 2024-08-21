# Modules
import os
import csv

print("Election Results")
print("-------------------------")

# Set path for file
csvpath = r"Pypoll/Resources/election_data.csv"
# csvpath = os.path.join("..","Resources", "budget_data.csv")

column_index_0 = 0
column_index_1 = 1
column_index_2 = 2

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

    # The total number of votes cast
    Total_vote = [row[column_index_0] for row in csvreader]
    print("Total Votes: " + str(len(Total_vote)))
    print("-------------------------")

    # A complete list of candidates who received votes
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    # Initialize an empty set to store unique candidates
    candidates_set = set()
    
    # Iterate over each line in the file
    for row in csvreader:
        # Split the line by comma to extract the candidate name
        candidate = row[2]        
        # Add the candidate to the set
        candidates_set.add(candidate)

        #Print the list of candidates
    print("List of candidates who received votes:")
    for candidate in candidates_set:
        print(candidate)
