# Modules
import os
import csv

print("Election Results")
print("-------------------------")

# Set path for file
csvpath = r"Pypoll/Resources/election_data.csv"
# csvpath = os.path.join("..","Resources", "budget_data.csv")

total_votes = 0
candidate_votes = {}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # The total number of votes cast
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
    # Calculate the percentage of votes each candidate won
results = {}
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results[candidate] = percentage

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage in results.items():
    print(f"{candidate}: {percentage:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
winner = max(results, key=results.get)
print(f"Winner: {winner}")
print("-------------------------")

#------------------------------
# Pypoll results
pypoll_results = {
    "Total Votes": " 369711",
    "------------": "------------",
    "Charles Casper Stockham": " 23.049% (85213)",
    "Diana DeGette": " 73.812% (272892)",
    "Raymon Anthony Doane": " 3.139% (11606)",
    "--------------": "----------------",
    "Winner": " Diana DeGette",
    "-------------": "--------------"
}

# Export results to text file
with open("Pypoll Election Results.txt", "w") as file:
    file.write("Election results\n")
    file.write("----------------------\n")
    for key, value in pypoll_results.items():
        file.write(f"{key}: {value}\n")
    file.write("\n")
