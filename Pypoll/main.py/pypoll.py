import csv

# create file path
csvpath = "C:/Users/rober/OneDrive/Documents/data_bootcamp/homework/ds_apr2024_3_python/Pypoll/Resources/election_data.csv"
output_file = "Analysis"

# set variables
total_votes = 0

candidate_options = []
candidate_votes = {}

winner = ""
winning_votes = 0

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    for row in csvreader:

        # add votes together
        total_votes = total_votes + 1

        names = row[2]

        # figure out candidates
        if names not in candidate_options:
            candidate_options.append(names)
            candidate_votes[names] = 0

        candidate_votes[names] = candidate_votes[names] + 1
    
    # print first part of results
output = f"""Election Results
-------------------------
Total Votes: {total_votes}
---------------------------\n"""

for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    vote_percentage = votes / total_votes * 100

    # find winner
    if (votes > winning_votes):
        winning_votes = votes
        winner = candidate

    # create final tally
    voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    final_tally = voter_output
    # print the final tally
    output2 = (final_tally)
    output += output2

# print third part of results
output3 = f"""-----------------
Winner: {winner}
--------------------"""

output += output3

print(output)

with(open("Election Results.txt", 'w') as f):
    f.write(output)








            





