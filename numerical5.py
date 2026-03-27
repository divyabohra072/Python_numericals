'''Assume a college is conducting a Student Council Election with multiple candidates. Votes are collected booth-wise and class-wise.vYou are given a list where each element represents the number of votes received by a candidate in different booths.
 Example:
votes = [[120, 135, 150], [98, 110, 105], [140, 160, 155]]
(Each inner list = votes from Booth 1, Booth 2, Booth 3 for each candidate)'''

'''Write a program using “for loop” to:

Calculate the total votes for each candidate.
Display the winner (candidate with maximum total votes).

Print results in this format:
Candidate 1 Total Votes: ___  
Candidate 2 Total Votes: ___  
Candidate 3 Total Votes: ___  
Winner: Candidate ___'''


#Code
votes = [[120, 135, 150], [98, 110, 105], [140, 160, 155]]

totals = [0, 0, 0]

for i in range(len(votes)):
    candidate_total = 0
    for booth_votes in votes[i]:
        candidate_total += booth_votes
    totals[i] = candidate_total

winner_index = 0
max_votes = totals[0]

for i in range(1, len(totals)):
    if totals[i] > max_votes:
        max_votes = totals[i]
        winner_index = i

print("Candidate 1 Total Votes:", totals[0])
print("Candidate 2 Total Votes:", totals[1])
print("Candidate 3 Total Votes:", totals[2])
print("Winner: Candidate", winner_index + 1)
print("Divya Bohra, 2581130")
      

