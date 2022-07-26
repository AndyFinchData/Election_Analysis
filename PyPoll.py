
# Add dependencies
import csv
import os




#The data we need to retrieve
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_load
file_to_save = os.path.join("Election_Analysis","Election_analysis.txt")

#Open the elction results and read the file
    with open(file_to_load) as election_data:
    #To do: Read and analyze the data here:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote




