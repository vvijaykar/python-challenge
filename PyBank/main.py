# Dependencies 
import os 
import csv

# File Path 
csvpath = os.path.join("Data", "budget_data_2.csv")


# csvpath, 'r' , newline=""
# Read csv file 
with open(csvpath, 'r' , newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
   
    #Reading header data in csv_reader
    csvreader = next(csvreader) 
   
    #Initializing values
    months = []
    revenue = 0 
    max_profit = 0 
    min_profit = 0 

    for row in csvreader: 
        months.append(row[0])

        revenue = revenue + int(row[1])

        if(max_profit < int(row[1])):
            max_profit = int(row[1])
            max_profit_month = row[0]

        if(min_profit > int(row[1])):
            min_profit = int(row[1])
            min_profit_month = row[0]

           
print("--------------------------------------------")
print(f"Total Months: {months} ")
print(f"Total Revenue : $ {revenue}")
print(f"Average Change : ${round(revenue/len(months),2)}")
print(f"Greatest Increase in Profits : {max_profit_month} ({max_profit})")
print(f"Greatest Decrease in Profits : {min_profit_month} ({min_profit})")

file = open('outp[ut.txt', 'w')

file.write("Financial ANalysis")
file.write("\n---------------------------------------")
file.write("\nTotal Month: " + str(len(months)))
file.write("\nTotal Revenue: $" + str(revenue))
file.write("\nAverage Change : $" + str(round(revenue/len(months),2)))
file.write("\nGreatest Increase in Profits : " + str(max_profit_month) + "(" + str(max_profit) + ")")
file.write("\nGreatest Decrease in Profits : " + str(min_profit_month) + "(" + str(min_profit) + ")")

file.close()