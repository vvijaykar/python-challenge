import os 
import csv

csvpath = os.path.join("Data", "election_data_2.csv")


votes = 0 
candidates = []
vote_count = []
vote_count_winner = 0

with open(csvpath, newline = "") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)

    for row in csvreader:

        votes = votes + 1

        if (row[2] not in candidates):
            candidates.append(row[2])
            vote_count.append(0)


        candidate_index = candidates.index(row[2])
        vote_count[candidate_index] += 1 

    print("Election Results")
    print("--------------------------------------------")
    print(f"Total Votes: {votes}")

    for y in range(len(candidates)):
        vote_percent = round((vote_count[y]/votes) * 100, 3)
        print(f"{candidates[y]}: {vote_percent}% ({vote_count[y]})")
        if(vote_count_winner < vote_count[y]):
            vote_count_winner = vote_count[y]
            winner = candidates[y]

    print("--------------------------------------------")
    print(f"Winner: {winner}")
    print("--------------------------------------------")

file = open('output.txt', 'w')

file.write("Election Results")
file.write("\n-------------------------------------------")
file.write("\nTotal votes:" + str(votes))
file.write("\n-------------------------------------------")

for j in range(len*(candidates)):
    vote_percent = round((vote_count[j]/votes) * 100, 3)
    file.write("\n" + str(candidates[j]) + " : " + str(vote_percent) + "% (" + str(vote_count[j]) + ")")
    
file.write("\n-------------------------------------------")
file.write("\nWinner: " + str(winner))
file.wrtie("\n-------------------------------------------")

file.close()