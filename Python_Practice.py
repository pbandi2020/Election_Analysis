print("Hello Pyton Program")

import csv
import os

# Declare the file path 
# print(os.path.join("..", "Resources", "election_results.csv"))
in_file = os.path.join("Resources","election_results.csv")
out_file = os.path.join("PyPoll_Practice_results.txt")

#Total votes variable
tot_votes = 0

#Variable to list the candidate


#Open the input file. Using the with statement closes the file automatically
with open(in_file) as election_data:
    print(election_data)

my_list = []

with open(out_file, "w") as txt_file:
   

    header_row =(
        f"\nElection Analysis\n"
         )

    print(header_row)
    txt_file.write(header_row)
    
    data_row = (
        f"\nArapahoe\n"
        f"Denver\n"
        f"Jefferson\n"

    )

    txt_file.write(data_row)
    # txt_file.write("Arapahoe,")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson, ")
    
   
  
   