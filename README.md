# python-challenge

## Background

For this challenge, my tasks were to create and clone a Git repository for use in storing the files necessary to complete the following analyses: 

* PyBank: Analysis on monthly Profit/Loss data
* PyPoll: Analysis on election result

## PyBank

![Revenue](Images/revenue-per-lead.png)

* For PyBank, the challenge was creating a Python script to analyze the financial records of a company. We were given a financial dataset called "budget_data.csv". The dataset was composed of two columns: "Date" and "Profit/Losses".

* The task was to create a Python script that analyzes the records to calculate each of the following values:

    * The total number of months included in the dataset
    * The net total amount of "Profit/Losses" over the entire period
    * The changes in "Profit/Losses" over the entire period, and then the average of those changes
    * The greatest increase in profits (date and amount) over the entire period
    * The greatest decrease in profits (date and amount) over the entire period

* The results shoukld be as follows:

```text
Financial Analysis

----------------------------

Total Months: 86

Total: $22564198

Average Change: $-8311.11

Greatest Increase in Profits: Aug-16 ($1862002)

Greatest Decrease in Profits: Feb-14 ($-1825558)
```

## PyPoll

![Vote_Counting](Images/Vote_counting.png)

* For PyPoll, the challenge was helping a small, rural town modernize its vote-counting process. We were given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". The task was to create a Python script that analyzes the votes and calculates each of the following values:

    * The total number of votes cast
    * A complete list of candidates who received votes
    * The percentage of votes each candidate won
    * The total number of votes each candidate won
    * The winner of the election based on popular vote

* The results shoukld be as follows:

```text
Election Results

-------------------------

Total Votes: 369711

-------------------------

Charles Casper Stockham: 23.049% (85213)

Diana DeGette: 73.812% (272892)

Raymon Anthony Doane: 3.139% (11606)

-------------------------

Winner: Diana DeGette

-------------------------
```