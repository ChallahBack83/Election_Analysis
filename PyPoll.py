# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies
import csv
import os

# Assign a variable for the file to load from a path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable for the file to save to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Set variable to 0 to total the votes

total_votes = 0

# Declare new list
candidate_options = []

# Declare new dictionary 
candidate_votes = {}

#declare a variable that holds an empty string value for the winning candidate
winning_candidate = ""
    
#declare a variable for the winning count equal to zero
winning_count = 0

#declare a variable for the winning percentage equal to zero
winning_percentage = 0

# Open the election results and read the file.

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read the header row 
    
    headers = next(file_reader)
    
    # Print each row in the CSV file 
    for row in file_reader:

        # Add to vote count
        total_votes += 1
        
        # print candidate name for each row
        candidate_name = row[2]

        # if candidate does not match existing candidate
        if candidate_name not in candidate_options:
           
            # add to list of candidates.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1 

with open(file_to_save, "w") as txt_file:
 
    # After opening the file print final vote count to terminal             

    election_results = (

        f"\nElection Results\n"

        f"-----------------------------\n"

        f"Total Votes: {total_votes:,}\n"
                
        f"-----------------------------\n")
    
    print(election_results, end="")

    # Save the final vote count to the text file

    txt_file.write(election_results)
   
    # for loop iterate through candidate options & get name
    for candidate_name in candidate_votes:

        # use for loop variable retrieve votes of candidate from candidate_votes
        votes = candidate_votes[candidate_name]

        # calculate percentage of vote count
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # print candidate name and results            
     
        print(candidate_results)

        # save candidate results to text file
    
        txt_file.write(candidate_results)

        # Determine winning vote and percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name

    # Print winning candidates to terminal
    winning_candidate_summary = (

        f"-----------------------------\n"

        f"Winner: {winning_candidate}\n"

        f"Winning Vote Count: {winning_count:,}\n"

        f"Winning Percentage: {winning_percentage:.1f}%\n"

        f"-----------------------------\n")

    print(winning_candidate_summary)   
    
    # Save winning candidate's results to text file.

    txt_file.write(winning_candidate_summary)

