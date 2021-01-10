import datetime as dt
import csv
import os

# print the current time
current_datetime = dt.datetime.now()
print(f'Current time is: {current_datetime}')

#  Declare the file path - method one

# input_file = "Resources\election_results.csv"
# election_data = open(input_file,"r")
# print(election_data)

# Declare the file path - methode two

input_file = os.path.join("Resources\election_results.csv")

#Declare an output file path
output_file = os.path.join("election_analysis.txt")

#Calculat the total votes
with open(input_file,"r") as election_data:
    # print(election_data)


#OPen o/p file for printing summary
with open(output_file,"w") as election_results:
    # print(election_results)



