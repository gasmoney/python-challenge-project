import os 
import csv

csv_path = os.path.join("Data", "election_data.csv")
final_file = os.path.join("election_results.txt")

total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0

with open(csv_path, newline='') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    print(csv_reader)

    csv_header = next(csv_reader)

    print(f"Election Header: {csv_header}")

    for row in csvfile:

        total_votes += 1

        r = row.split(",")

        if r[2].strip() == "Khan":
            khan_votes += 1

        elif r[2].strip() == "Correy":
            correy_votes += 1

        elif r[2].strip() == "Li":
            li_votes += 1

        elif r[2].strip() == "O'Tooley":
            tooley_votes += 1

khan_percent = khan_votes/total_votes        
correy_percent = correy_votes/total_votes
li_percent = li_votes/total_votes
tooley_percent = tooley_votes/total_votes

candidates = {'Khan': khan_votes, 'Correy': correy_votes, 'Li': li_votes, 'O\'Tooley': tooley_votes}
winner = max(candidates, key=candidates.get)

output = (
    f"\nElection Results\n"
    f"---------------\n"
    f"Total Votes Cast: {total_votes}\n"
    f"---------------\n"
    f"Khan: {'{0:.3%}'.format(khan_percent)} ({khan_votes})\n"
    f"Correy: {'{0:.3%}'.format(correy_percent)} ({correy_votes})\n"
    f"Li: {'{0:.3%}'.format(li_percent)} ({li_votes})\n"
    f"O'Tooley: {'{0:.3%}'.format(tooley_percent)} ({tooley_votes})\n"
    f"----------------\n"
    f"Winner: {winner}\n"
    f"----------------\n")

print(output)

with open(final_file, "a") as txt_file:
    txt_file.write(output)

#I moved the csv election data file from its location in the pypoll folder when I wrote this code because of its size