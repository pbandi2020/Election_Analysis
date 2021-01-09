# Election_Analysis

## Overview of Project
This project is focused on elections data analysis. The key metric analyzed across multiple dimensions is the vote count. Let's take a look at diffrent points of view for elections data and how a winner is identifies based on popular votes registered by citizens across the county for a particular state. There are certain assumations within data analysis which we will discuss in our summary sections for the project.

### Purpose & Scope of this Effort
1. Fact 1 - To provide a summary of total votes registered across all counties and candidates.
2. Fact 2 - To provide a summary of total popular votes registered by each county
3. Fact 3 - To provide a summary of total popular votes registered by candidate
4. Fact 4 - Based on popular votes received to identify the winner
  * By Candiate
  * By County


# Results
### Election Analysis Report
* Our challenge 3 analysis focused on a single dimension analysis. As per out output her is what is infered from from output.
* Turnaround of votes or the county that received the most popular votes is **Denver** county. Over **82%** of votes were recorded in this county and as per our analysis the winner of the election is **Diana DeGette** who received **272,892** votes of the total received popular votes of **306,055** registered across all counties. An out text file is aviable in **Analysis\election_results.txt** and when executing the program the same is printed to the terminal. 

<img src=/Resources/RuntimeComparisonTable.png alt="Runtime Analysis Report"/>
 
                                                                                                                                                                      
### Challenges and Difficulties Encountered
* I am fairly new to Python programming and hence getting the right syntax, understanding the error and debugging was the most challenging part of this exercise but the exampled is the module was very helpful in getting to completion of the project. 

### My Conclusion Summary on the Challenge Results 
1. To be mre accurate in termining the winner if the election the candidate results must be broken by county and candidate to determine the winner
2. The data provided only has county dimension. So we really do not know which state the county is in hence our analysis is with the assumtion all these counties are in one state.
3. In general candidates do not context in multiple counties but our results by candidate is taking all counties into account. Hence declaring a winner by total registered votes across counties is not a proper way of determining a winner of the elections. And not knowing the state associated to the county is another gap in data avaiable to declare a winner.
4. Next, since we do not know how many registered voters are there is each county, we cannot really determine the percentage of votes recorded. In other words **Expected Vs Registered **
