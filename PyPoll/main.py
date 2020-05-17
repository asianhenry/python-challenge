
import os
import csv
#need this to count votes
from collections import Counter

# Read in the CSV file
csvpath = os.path.join('../../''election_data.csv')
with open(csvpath) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #variable for vote counts
    totalvotes = 0

    candidate = []
    
    # Loop through the data
    for row in csvreader:
        totalvotes += 1
        candidate.append(row[2])


#O.O this creates a dictionary with the candidate names (keys) and the number of votes
votes = Counter(candidate)

#we can convert the seperate dictionary elements into lists (keys and values)
candidatelist = list(votes.keys())
votecount = list(votes.values()) 

#we create a list with the calculated percentage of votes
#also you this format to present percentage values with 3 decimal places
votepercentages = ["{:.3f}".format(count/totalvotes*100) for count in votecount]

#just printing text
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")

#print out the text for each candidate
for i in range(len(candidatelist)):
    print(f"{candidatelist[i]}: {votepercentages[i]}% ({votecount[i]})")

print("-------------------------")  

#find the vote winner
for i in range(len(candidatelist)): 
    if max(votecount) == votecount[i]:
        print(f"Winner: {candidatelist[i]}")

print("-------------------------")



  #Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------

#this creates and writes a txt file with the code output
# x creates, a appends, w overwrites, r is read only
# w+ will overwrite or create a file if not there
with open("election_results.txt", "w+") as f:

    print("Election Results",file=f)
    print("-------------------------",file=f)
    print(f"Total Votes: {totalvotes}",file=f)
    print("-------------------------",file=f)


    for i in range(len(candidatelist)):
        print(f"{candidatelist[i]}: {votepercentages[i]}% ({votecount[i]})",file=f)

    print("-------------------------",file=f)  


    for i in range(len(candidatelist)): 
        if max(votecount) == votecount[i]:
            print(f"Winner: {candidatelist[i]}",file=f)

    print("-------------------------",file=f)