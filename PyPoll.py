import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

#Declare an empty dictionary:
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        #If the candidate name does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #2 Begin tracking each candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1


# Print the candidate list.
print(candidate_options)
print(candidate_votes)


# 3. The percentage of votes each candidate won
#Iterate through the candidate list.
for candidate_name in candidate_votes:
    #Retrieve vote coiunt of a candidate.
    votes = candidate_votes[candidate_name]
    #calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print candidate name and percentage of votes
    print(f'{candidate_name}: received {vote_percentage}% of the vote.')
    

# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote




