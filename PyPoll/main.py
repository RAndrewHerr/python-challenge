#Import modules
import os
import csv

#Path to raw data file
election_csv = os.path.join('.', 'Resources', 'election_data.csv')

#Create Lists to store retreived data from csv
vote_by_id_list = []
vote_by_candidate_name_list = []

#Open the source file in read mode
with open(election_csv, 'r') as csvfile:

    #Split data by comma delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    #Loop through csv data to populate lists
    for row in csvreader:
        vote_by_id_list.append(int(row[0]))
        vote_by_candidate_name_list.append(row[2])

#Use Counter to create dictionary that holds the votes per candidate
from collections import Counter

vote_count = Counter(vote_by_candidate_name_list)

#Create lists to analyze vote data
candidate_names = list(vote_count.keys())
candidate_votes = list(vote_count.values())

#Create variables for results
number_of_candiates = len(candidate_names)
total_votes_by_id = (len(vote_by_id_list))
winner_by_popular_vote = max(vote_count, key=vote_count.get)

#List comprehension to calculate percentage of total vote by candidate 
percent_of_total_vote = [round(((x/total_votes_by_id) * 100), 3) for x in candidate_votes]

#Print analysis results to terminal
print()
print("Election Results")
print()
print("----------------------------")
print()
print(f"Total votes: {total_votes_by_id}")
print()
print("----------------------------")
print()
print(f"{candidate_names[0]}: {percent_of_total_vote[0]}% ({candidate_votes[0]})")
print()
print(f"{candidate_names[1]}: {percent_of_total_vote[1]}% ({candidate_votes[1]})")
print()
print(f"{candidate_names[2]}: {percent_of_total_vote[2]}% ({candidate_votes[2]})")
print()
print("----------------------------")
print()
print(f"Winner: {winner_by_popular_vote}")
print()
print("----------------------------")
print()

#Path to output file
results_txt = os.path.join('.', 'Analysis', 'pypoll_results.txt')

#Open the output file in write mode
with open(results_txt, 'w') as textfile:

    textfile.write("Election Results\n")
    textfile.write("\n")
    textfile.write("----------------------------\n")
    textfile.write("\n")
    textfile.write(f"Total votes: {total_votes_by_id}\n")
    textfile.write("\n")
    textfile.write("----------------------------\n")
    textfile.write("\n")
    textfile.write(f"{candidate_names[0]}: {percent_of_total_vote[0]}% ({candidate_votes[0]})\n")
    textfile.write("\n")
    textfile.write(f"{candidate_names[1]}: {percent_of_total_vote[1]}% ({candidate_votes[1]})\n")
    textfile.write("\n")
    textfile.write(f"{candidate_names[2]}: {percent_of_total_vote[2]}% ({candidate_votes[2]})\n")
    textfile.write("\n")
    textfile.write("----------------------------\n")
    textfile.write("\n")
    textfile.write(f"Winner: {winner_by_popular_vote}\n")
    textfile.write("\n")
    textfile.write("----------------------------\n")