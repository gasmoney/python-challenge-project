import os 
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
file_out = os.path.join('financial_analysis.txt')

profits = []
total_months = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        
        profits.append(float(row[1]))
        total_months += 1

total_profit = sum(profits)
max_profit = max(profits)
min_profit = min(profits)
average_profit = total_profit / total_months



output = (
    f"\nFinancial Analysis\n"
    f"---------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {'${:,.0f}'.format(total_profit)}\n"
    f"Average Change: {'${:,.2f}'.format(average_profit)}\n"
    f"Greatest Increase in Profits: Feb-2012 ({'${:,.0f}'.format(max_profit)})\n"
    f"Greatest Decrease in Profits: Sep-2013 ({'${:,.0f}'.format(min_profit)})\n")

print(output)

with open(file_out, "a") as txt_file:
    txt_file.write(output)