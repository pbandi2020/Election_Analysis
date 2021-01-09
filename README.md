# Election_Analysis

## Overview of Project
This project is focused in elections data analysis. The key metric analysed across multiple dimensions is the vote count. Let's take a look at the diffrent view point of elections data and how a winner is identifies based on popular votes registered by citizens across county for a particular state. There are certain assumations with the data analysis which we will discuss in our summary sections for the project.

### Purpose & Scope of this Effort
- Fact 1 - To provide a summary of total votes registered across all counties and candidates.
- Fact 2 - To provide a summary of total popular votes registered by county
- Fact 3 - To provide a summary of tatal popular votes registered by candidate
- Fact 4 - Based on populat votes received to identify the winner
 1. By Candiate
 2. By County


# Results
### Election Analysis Report
* Our challenge 3 analysis focused on a single dimension analysis. As per out output her is what is infered from from output.
* Turnaround of votes or the county that received the most popular votes is **"Denver"** county. Over **"82%"** of votes vered recorded in this county and as per out analysis the winner of the election is **"Diana DeGette"** who received **"272,892"** votes of the total **"306,055"** of total votes registered across all counties.

<!--![RunTime Comparison Report](/Resources/RuntimeComparisonTable.png) -->

<img src=/Resources/RuntimeComparisonTable.png alt="Runtime Analysis Report"/>
 
### VBA Challenge Results - Most efficient refactored code
* As discussed earlier, a final result can be achived by many diffrent coding practice. The result achieved using an array for the ticker and using a single loop is the most efficient logic. However, this logic is with the assumption the dataset is sorted by ticker column and closing date. The key to data analysis is sorting the dataset. This is a step we did not perrform as the 2017 & 2018 dataset provided for module 2 challenge was sorted and we knew that we had only 12 stocks to process for end results. 

 <table>
 <tr>   
    <td align="center"> 2017 VBA_Challege output </td>
    <td align="center"> 2018 VBA_Challege output</td>
  </tr> 
  <tr>   
    <td valign="top"> <img src="/Resources/2017%20AllstocksAnalysisRefactor.png" width="500" /> </td>
    <td valign="top"> <img src="/Resources/2018%20AllstocksAnalysisRefactor.png" width="500" /> </td>
  </tr>     
</Table> 

### Comparing the VBA Challenge results to two other alternate logic
* One result below uses nested loop logic. The other option is very similar to the final refactored code, the only diffrence is where the output data table to created.

<Table>
 <tr>   
    <td align="center"> AllStocksAnalysisRefactor V2 </td>
    <td align="center"> AllStocksAnalysisRefactor V1 </td>
  </tr> 
  <tr>   
    <td valign="top"> <img src="/Resources/2018AllStocksAnalysisRefactorV2.png" width="500" /> </td>
    <td valign="top"> <img src="/Resources/2018AllStocksAnalysisRefactorV1.png" width="500"  width="500" /> </td>
  </tr>     
</Table> 
                                                                                                                                                                         
### Challenges and Difficulties Encountered
* As a programmer, we look for **"What, When, Why, Where and Who "** as part of the requirements. This exercise was **"very challenging as the HOW was defined"**. Especially it took  several debugging activities to determine logical error in step 3d. As I was using a "nested if" to write the logic and following the directions in step 3d was resulting in a wrong index and wrong output. Since the pseudo-code was not very clear and step 2a & 2b asked to use "nested For Loop" was misguiding the logical flow.   

## Summary
  - Our returns are based on closing prices on the first and last market days of the year. Based on this data we may show postive or negative returns for a full year, however we would not know weekly/bi-weekly, monthly or quaterly trends. Just by looking at EOY returns will allow for portfolio changes yearly whereby missing out on some potential profits/limiting losses during shorter frequencies.
  - Having availability of hourly trends will also help in some profit taking during the day or potentailly readjusting portfolios
  
