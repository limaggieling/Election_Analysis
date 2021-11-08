# Election_Analysis
VS Code with Python

# Overview
**Purpose
For our script, we needed to be able to output the following 

Total number of votes cast
A complete list of candidates who received votes
Total number of votes each candidate received
Percentage of votes each candidate won
The winner of the election based on popular vote

**Background
Using the csv file election_data.csv, we needed to extract, calcuate, and print the election information.

# Results

![electionresults](Election_Analysis/Resources/electionresults.png)

Total Votes were based on total number of voters (unique ids)
Votes per County were measured by using the county name, calulating the percentage of votes cast divided by total number of votes
County with largest voter turnout was measured by extracting which county had the largest number of votes cast
Number of votes cast were extacting by counting the repetitions of each county 
Percentage of votes cast was calculated by using the total votes for that candidate divided by the total voters
Winning candidate was supposed to be measured by assessing total number of votes won for that candidate, along with highest percentage of votes per candidate

# Summary

**Challenges
Regarding my irregular results, I found a small issue that I could not fix in time. I realized that the winners data was outputting the county votes data of denver and not the candidate results. Strict on time, I submitted what I had in advanced, but upon observation, realized my mistake. To correct the outcome, I would go through my code at the sections that address the variables of county vs candidate and determine where I may have entered the wrong variables. All in all, had I been more careful to take the time to enter my variables and used additional commentry, I believe I could have avoided this mistake. 

**Conclusions
The true winner of the election was Diana DeGette.
The script is capable of being applied to a larger election. It can be adjusted for use nation-wide because it is versitile enough to loop through any unique number of candidates and counties. We can simply adjust those variables to reflect per state or city.
