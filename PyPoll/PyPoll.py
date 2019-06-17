# Import modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources" , "election_data.csv")

# Create lists to store data
voter_id = []
county = []
candidate = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
    # Count total number of votes cast
    totalvoters = len(voter_id)

    # unique list of candidates who recieved votes
    unique_candidates = list(dict.fromkeys(candidate))

    KhanCount = candidate.count("Khan")
    KhanPercent = KhanCount / totalvoters

    CorreyCount = candidate.count("Correy")
    CorreyPercent = CorreyCount / totalvoters

    LiCount = candidate.count("Li")
    LiPercent = LiCount / totalvoters

    OTooleyCount = candidate.count("O'Tooley")
    OTooleyPercent = OTooleyCount / totalvoters

    def winner(list):
        return max(set(list), key = list.count)

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + format(totalvoters, ","))
    print("----------------------------")
    print("Khan: " + format((KhanPercent*100), ".0f") + "% (" + format(KhanCount, ",") + ")" )
    print("Correy: " + format((CorreyPercent*100), ".0f") + "% (" + format(CorreyCount, ",") + ")" )
    print("Li: " + format((LiPercent*100), ".0f") + "% (" + format(LiCount, ",") + ")" )
    print("O'Tooley: " + format((OTooleyPercent*100), ".0f") + "% (" + format(OTooleyCount, ",") + ")" )
    print("----------------------------")
    print("Winner: " + winner(candidate))

    file = "PyPoll_Report.txt"
    with open(file,'w') as f:
        print("Election Results", file=f)
        print("----------------------------", file=f)
        print("Total Votes: " + format(totalvoters, ","), file=f)
        print("----------------------------", file=f)
        print("Khan: " + format((KhanPercent*100), ".0f") + "% (" + format(KhanCount, ",") + ")" , file=f)
        print("Correy: " + format((CorreyPercent*100), ".0f") + "% (" + format(CorreyCount, ",") + ")" , file=f)
        print("Li: " + format((LiPercent*100), ".0f") + "% (" + format(LiCount, ",") + ")" , file=f)
        print("O'Tooley: " + format((OTooleyPercent*100), ".0f") + "% (" + format(OTooleyCount, ",") + ")" , file=f)
        print("----------------------------", file=f)
        print("Winner: " + winner(candidate), file=f)
        f.close()