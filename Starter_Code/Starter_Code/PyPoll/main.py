#  start with dependencies
import csv
import os


# Create an grab file patha

filepath2= 'Resources/election_data.csv'
with open(filepath2) as csvfile2:
    csvreader = csv.reader(csvfile2, delimiter =',')

    csv_header = next(csvreader)

    candidates= [candidate[2] for candidate in csvreader]
# Grab Votecount
    vote_count = len(candidates)
    print('Total Votes : ', vote_count)

    candidatelist = [[candidate, candidates.count(candidate)] for candidate in set(candidates)]

    for candidate in candidatelist:
        percent_votes = (candidate[1]/vote_count) *100
# Print results
filepath = os.path.join('.', 'Resources', 'PyPoll_Results.txt')
with open(filepath, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {vote_count}", file=text_file)
    print("-------------------------", file=text_file)






    

 









    

    













    


