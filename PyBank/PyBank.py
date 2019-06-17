# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources" , "budget_data.csv")

# Create lists to store data
month = []
profit_loss_table = []
NewPL = []
OldPL = []
amount_change = []
month_adjusted = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # Loop through records
    for row in csvreader:
       month.append(row[0])
       profit_loss_table.append(int(row[1]))
    
    total_amount = sum(profit_loss_table)
    NewPL = profit_loss_table[1:]
    OldPL = profit_loss_table[:-1]

    # Option 1 to find Average Change (newest value - oldest value) / (# of months -1)
    #print("----------------------------")
    #print(profit_loss_table[0])
    #print(profit_loss_table[-1])
    #print("----------------------------")
    
    # Option 2 to find Average Change using lists:
    amount_change = [new - old for (new, old) in zip(NewPL, OldPL)]
    #amount_change_test = profit_loss_table[]
    avg_change = round((sum(amount_change) / len(amount_change)),2)
    
## Greatest Profit and Loss Values
    # adjust month list to fit the amount_change list. It takes out the first value 
    # since the first month does not have a change.
    month_adjusted = month[1:]

    # find the index number of the highest profit and loss amount in amount_change list
    MaxIndex = amount_change.index(max(amount_change))
    MinIndex = amount_change.index(min(amount_change))

    MaxProfitMonth = month_adjusted[MaxIndex]
    MinProfitMonth = month_adjusted[MinIndex]
    MaxProfit = amount_change[MaxIndex]
    MinProfit = amount_change[MinIndex]

# print final hw
    print("----------------------------")
    print("Finacial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(month)))
    print("Total: " + "$" + format(total_amount, ","))
    print("Average Change: " + "$" + format(avg_change,',.2f'))
    print("Greatest Increase in Profits: " + MaxProfitMonth + " ($" + format(MaxProfit,',.2f') + ")")
    print("Greatest Decrease in Profits: " + MinProfitMonth + " ($" + format(MinProfit, ',.2f') + ")")
    print("----------------------------")

file = "PyBank_Report.txt"
with open(file,'w') as f:
    print("----------------------------",file=f)
    print("Finacial Analysis",file=f)
    print("----------------------------",file=f)
    print("Total Months: " + str(len(month)),file=f)
    print("Total: " + "$" + format(total_amount, ","),file=f)
    print("Average Change: " + "$" + format(avg_change,',.2f'),file=f)
    print("Greatest Increase in Profits: " + MaxProfitMonth + " ($" + format(MaxProfit,',.2f') + ")",file=f)
    print("Greatest Decrease in Profits: " + MinProfitMonth + " ($" + format(MinProfit, ',.2f') + ")",file=f)
    print("----------------------------",file=f)
    f.close()