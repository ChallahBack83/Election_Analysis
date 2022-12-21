# Election_Analysis

## Project Overview

The purpose of this project was to comb through election data for 3 counties in Colorado and identify the winning candidate for this congressional election as well as provide the amount of votes each candidate received and the amount of votes cast in each county. By pulling all the information we can also identify which county had the largest county turnout which will help plan for future elections. The Challenge provided us with the code that tallied the candidate data. Therefore, I could focus on the county data. Using the knowledge I learned through the exercises, I pulled the percentage of and total votes by county and indentified the county with the largest voter turnout.  

## Election-Audit Results

In order to collect the data by county, I created a list for the counties, a dictionary for the votes by county, and variables for the largest county and county turnout. 
```
# 1: Create a county list and county votes dictionary.
counties = []
county_votes = {}
```
```
# 2: Track the largest county and county voter turnout.
largest_county = ""
winning_county = 0
county_turnout = 0
```
Under the 'for loop' but before the if statement, I inserted script to extract the county name from each row.  This allowed me to then create an if statement to pull the unique county names into their list and start tallying votes by county under the 'for loop' that iterates through the rows of data.
```
# 3: Extract the county name from each row.
        county_name = row[1]
```
```
 # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in counties:
            
            # 4b: Add the existing county to the list of counties.
            counties.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```
I then wrote code to pull the county votes by county, calculate the percentages of votes by county, determine the largest county, print all the information to the terminal, and write everything to the appropriate text file.  The following code shows these additions to the script.
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
I corrected the path to write to the correct text file and ran the code. After some reformatting, the code printed successfully to the [Terminal](https://github.com/ChallahBack83/Election_Analysis/blob/main/resources/results_command_line.png). To view the results, you can also access the [Election Results Text File](https://github.com/ChallahBack83/Election_Analysis/blob/main/analysis/election_analysis.txt). Below is a further breakdown of the specific results.

+ For this election, a total of 369,711 votes were cast across these three counties printing the following results:
    + ![Total Votes](https://github.com/ChallahBack83/Election_Analysis/blob/main/resources/Total%20Votes.png)
    + This information was gathered by iterating through all rows of election data and adding to the total vote count with the following code:
    +  
      ```  
      for row in reader:
          total_votes = total_votes + 1
      ```    
+ Out of the total 369,711 votes in this election, the vote breakdown by county is:
    + ![County Votes](https://github.com/ChallahBack83/Election_Analysis/blob/main/resources/Votes_County.png)
    + County percentage was calculated by dividing county voter turnout by the total votes in the election:
    + 
      ```     
      county_percentage = float(county_turnout) / float(total_votes) * 100
      ```    
+ Denver County had the largest percentage of voters at 82.8% with 306,055 total votes.
    + ![Largest County](https://github.com/ChallahBack83/Election_Analysis/blob/main/resources/Largest_County.png)
+ Out of the total 369,711 votes in this election, the vote breakdown by candidate is:
    + ![Candidate Votes](https://github.com/ChallahBack83/Election_Analysis/blob/main/resources/Votes_Candidate.png)
    + Percentage of votes by candidate was calculated the same way we determined percentage by county:
    + 
      ```     
      vote_percentage = float(votes) / float(total_votes) * 100
      ```    
+ According to these numbers, the winner of this congressional election is Diana DeGette with 73.8% of the vote.
    + ![Winning Summary](https://github.com/ChallahBack83/Election_Analysis/blob/main/resources/Winner_Summary.png)

## Election-Audit Summary

In summary, the code created to run the analysis of the congressional election has helped us pull vital statistics on votes by candidate and county and determine the winner of this election.  With minor changes, this code is transferable to use for future election data.  Some suggestions:

+  Currently the script pull the information based on indexing of the rows. We cannot guarantee all data will import the same, so we could import                      other dependencies, such as pandas, to create data frames. Then we can build in a script to identify data type and pull the necessary information based              on data type rather than index.
+  The current script doesn't account for error handling. We can account for that, coding in directions on how to deal with errors in the data. 
+  Perhaps we want to use this to handle different types of election data, such as from cities or states. Again, we could rename variables to make it less              dependent on county or candidate specifically and help it reference which ever data type we set with one change to the script rather than many.
