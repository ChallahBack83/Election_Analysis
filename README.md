# Election_Analysis

## Project Overview

The purpose of this project was to comb through election data for 3 counties in Colorado and identify the winning candidate for this congressional election as well as provide the amount of votes each candidate received and the amount of votes cast in each county.  By pulling all the information we can also identify which county had the largest county turnout which will help plan for future elections. The Challenge provided us with the code that tallied the candidate data. Therefore, I could focus on the county data.  Using the knowledge I learned through the exercises, I pulled the percentage of and total votes by county and indentified the county with the largest voter turnout.  

## Election-Audit Results


I then wrote code to pull the county votes by county, calculate the percentages of votes by county, determine the winning, or largest, county, print all the information to the terminal, and write everything to the appropriate text file.  The following code shows these changes in the script.
```
 # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
       
        # 6b: Retrieve the county vote count.
        county_turnout = county_votes[county_name]
       
        # 6c: Calculate the percentage of votes for the county.
        county_percentage = float(county_turnout) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {county_percentage:.1f}% ({county_turnout:,})\n")
           
        print(county_results, end="")

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_turnout > winning_county):
            winning_county = county_turnout
            largest_county = county_name        
           
    # 7: Print the county with the largest turnout to the terminal.
        
    largest_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")

    print(largest_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_summary)

```
I corrected the path to write to the correct text file and ran the code. After some reformatting, the code printed successfully to the [Terminal](https://github.com/ChallahBack83/Election_Analysis/blob/main/resources/results_command_line.png). To view the results, you can also access the [Election Results](https://github.com/ChallahBack83/Election_Analysis/blob/main/analysis/election_analysis.txt) text file.  Below is a further breakdown of the specific results.

+ How many votes were cast in the congressional election?
    + the
    + ![Total Votes](https://github.com/ChallahBack83/Election_Analysis/blob/main/resources/Total%20Votes.png)
    
+ Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct
    + the
    + ![County Votes](https://github.com/ChallahBack83/Election_Analysis/blob/main/resources/Votes_County.png)
    
+ Which county had the largest number of votes?
    + the
    + ![Largest County](https://github.com/ChallahBack83/Election_Analysis/blob/main/resources/Largest_County.png)
  
+ Provide breakdown of the number of votes and the percentage of the total votes each candidate received.
    + the
    + ![Candidate Votes](https://github.com/ChallahBack83/Election_Analysis/blob/main/resources/Votes_Candidate.png)
    
+ Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    + the
    + ![Winning Summary](https://github.com/ChallahBack83/Election_Analysis/blob/main/resources/Winner_Summary.png)

## Election-Audit Summary

provide business proposal to election commission o how this script can be used--with some modifications--for any election. 
give at least 2 examples of how the script can be modified.
