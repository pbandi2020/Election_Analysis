# A quick test before starting the code
# my_string = "Hello!"
# print(my_string)
#*********************************************************
#Election Analysis Psuedo Code
#********************************************************

# Instantiate the CSV API

import csv
import os
import datetime as dt

# Get the current / system time into a variable. 
systemtime = dt.datetime.now()

print(f"Date&Time: {systemtime}")


# Declare the file path 
# print(os.path.join("..", "Resources", "election_results.csv"))
input_file = os.path.join("Resources\election_results.csv")

#Declare an output file path
output_file = os.path.join("election_analysis.txt")

# Initialize the total vote count and create an empty list for candidatescandidate option and a empty dictionary for candidate votes
total_votes = 0

candidate_options = []
candidate_votes = {}

#Variables for Winning candidate, winning count and winning percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the input file. Using the with statement closes the file automatically
with open(input_file, newline="") as election_data:
    file_reader = csv.reader(election_data,delimiter = ",")

    # Read the header row and save into variable before starting to process the election data
    header = next(file_reader)

    # print(header)
    for i in file_reader:
        #sum the total votes
        total_votes += 1

        #candidate name for each row
        candidate_name = i[2]

        #Start with the first candidate in the spreadsheet to count the votes by candidate. This step is with assumtion the file is already sorted by candidate.
        if candidate_name not in candidate_options:
            #start populating the candidate options list
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] +=1

    # print(f'{candidate_name} - {total_votes}')
            
print(f'{candidate_options}')
print(f'{candidate_votes}')
print(total_votes)

#Wite the result to a textfile/outfile
with open(output_file,"w") as txt_file:

    election_results =(
        f"\nElection Results\n"
        f"-------------------\n"
        f"Total Votes: {total_votes:,} \n"
        f"-------------------\n"   )

    print(election_results)

    #write the elections result o/p to the text file
    txt_file.write(election_results)

    # Now lets find the winner and the winning percentage
    for i in candidate_votes:

        votes = candidate_votes[i]
        vote_percent = float(votes)/float(total_votes) * 100

        candidate_results = f"{i}, got a total of ({votes:,}) which equates to {vote_percent:.1f}% \n"

        print(candidate_results)

        #Save the text file
        txt_file.writelines(candidate_results)

        # finalizing the winner
        if (votes > winning_count) and (vote_percent > winning_percentage):
            winning_candidate = i
            winning_percentage = vote_percent
            winning_count = votes

    # print final summary
    winning_candidate_summary = (
        f"-----------------------------------------\n"
        f"Winning Candidate : {winning_candidate} \n"
        f"Winning Vote Count: {winning_count:,} \n"
        f"Won By            : {winning_percentage:.1f} %\n"
        f"--------------------------------------------\n"   )

    print(winning_candidate_summary)

    #complete the project by appending the winner result to he outputfile
    txt_file.write(winning_candidate_summary)







    

