import csv

# create file path
csvpath = "C:/Users/rober/OneDrive/Documents/data_bootcamp/homework/ds_apr2024_3_python/Pybank/Resources/budget_data.csv"

# set variables
month_count = 0
total_profit = 0

last_month_profit = 0
changes = []
month_changes = []

# open csv
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    csvheader = next(csvreader)

    # get every row of data after header
    for row in csvreader:

        # count months
        month_count += 1

        # sum the profit
        total_profit = total_profit + int(row[1])

        # find the changes in profit or loss
        if (month_count == 1):
            last_month_profit = int(row[1])

        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            last_month_profit = int(row[1])

    avg_change = round(sum(changes) / len(changes),2)

    max_change = max(changes)
    max_month_index = changes.index(max_change)
    max_month = month_changes[max_month_index]

    min_change = min(changes)
    min_month_index = changes.index(min_change)
    min_month = month_changes[min_month_index]

    # print analysis
    output = f"""Financial Analysis
-----------------------------
Total Months: {month_count}
Total: {total_profit}
Average Change: ${round(avg_change)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})"""
    
    print(output)

    with(open("Financial Analysis.txt", 'w') as f):
        f.write(output)