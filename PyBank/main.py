#Import modules
import os
import csv

#Path to raw data file
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

#Create Lists to store retreived data from csv
months_list = []
profit_loss_list = []
profit_loss_delta_list = []

#Open the source file in read mode
with open(budget_csv, 'r') as csvfile:

    #Split data by comma delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        months_list.append(row[0])
        profit_loss_list.append(int(row[1]))
    for row in range(len(months_list)-1):
        profit_loss_delta_list.append(profit_loss_list[row+1]-profit_loss_list[row])

#Create variables for analysis
months_total = len(months_list)
profit_loss_total = sum(profit_loss_list)
profit_loss_delta_avg = round((sum(profit_loss_delta_list) / (months_total - 1)), 2)
profit_loss_max = max(profit_loss_delta_list)
profit_loss_max_month = months_list[(profit_loss_delta_list.index(profit_loss_max)+1)]
profit_loss_min = min(profit_loss_delta_list)
profit_loss_min_month = months_list[(profit_loss_delta_list.index(profit_loss_min)+1)]

#Print analysis results to terminal
print()
print("Financial Analysis")
print()
print("----------------------------")
print()
print(f"Total Months: {months_total}")
print()
print(f"Total: ${profit_loss_total}")
print()
print(f"Average Change: ${profit_loss_delta_avg}")
print()
print(f"Greatest Increase in Profits: {profit_loss_max_month} (${profit_loss_max})")
print()
print(f"Greatest Decrease in Profits: {profit_loss_min_month} (${profit_loss_min})")
print()

#Path to output file
results_txt = os.path.join('.', 'Analysis', 'pybank_results.txt')

#Open the output file in write mode
with open(results_txt, 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("\n")
    textfile.write("----------------------------\n")
    textfile.write("\n")
    textfile.write(f"Total Months: {months_total}\n")
    textfile.write("\n")
    textfile.write(f"Total: ${profit_loss_total}\n")
    textfile.write("\n")
    textfile.write(f"Average Change: ${profit_loss_delta_avg}\n")
    textfile.write("\n")
    textfile.write(f"Greatest Increase in Profits: {profit_loss_max_month} (${profit_loss_max})\n")
    textfile.write("\n")
    textfile.write(f"Greatest Decrease in Profits: {profit_loss_min_month} (${profit_loss_min})\n")