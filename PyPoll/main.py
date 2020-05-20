
import os
import csv

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

#------------------------------------------------------------

#O.O this creates a dictionary with the candidate names (keys) and the number of votes
#from collections import Counter
#votes = Counter(candidate)

#we can convert the seperate dictionary elements into lists (keys and values)
#candidatelist = list(votes.keys())
#votecount = list(votes.values()) 

#ok so this is what I originally did. We aren't allowed to use imported libraries for this assignment, but I'll just leave this here

#------------------------------------------------------------

candidatelist = []

#use this loop to create a list with only unique candidate names
for x in range(len(candidate)):  
    if candidate[x] not in candidatelist: 
        candidatelist.append(candidate[x])

#use comprehensions! I originally used a for loop but should get into the practice of list comprehensions
#then set the initial values to zero
votecount = [0 for x in candidatelist]

#for y in range(len(candidatelist)):
#        votecount.append(int(0))    
        
#ok this took some thinking
#we use nested for loop to add a vote counter every time the candidate name appears in the original "candidate" list
for x in range(len(candidate)):
    for y in range(len(candidatelist)):
        if candidate[x] == candidatelist[y]:
            votecount[y] += 1


#we create a list with the calculated percentage of votes
#also you this format to present percentage values with 3 decimal places
votepercentages = ["{:.3f}".format(i/totalvotes*100) for i in votecount]

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