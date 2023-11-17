import os

import csv

csvpath = os.path.join("Resources","election_data.csv")

analysis = ("c:/Users/Allister Rebello/Desktop/Analysis Projects/Unit 03 - Python/Module 3/python-challenge/PyPoll/analysis")

output_file_path = os.path.join("analysis", "Financial_Analysis.txt")

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # Skip the header row
    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        print(row)
        
        voter_id, county, candidate = row
        
        # Count total votes
        total_votes += 1
        
        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Determine the winner
for candidate, votes in candidates.items():
    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

# Calculate the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = {"votes": votes, "percentage": round(percentage, 2)}

# Print results to the console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, data in candidates.items():
    print(f"{candidate}: {data['percentage']}% ({data['votes']})")
print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

# Save results to a text file
with open("Election_Results.txt", "w") as Output_File:
    Output_File.write("Election Results\n")
    Output_File.write("-------------------------\n")
    Output_File.write(f"Total Votes: {total_votes}\n")
    Output_File.write("-------------------------\n")
    for candidate, data in candidates.items():
        Output_File.write(f"{candidate}: {data['percentage']}% ({data['votes']})\n")
    Output_File.write("-------------------------\n")
    Output_File.write(f"Winner: {winner['name']}\n")
    Output_File.write("-------------------------\n")
