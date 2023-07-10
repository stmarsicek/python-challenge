#  start with dependencies
import csv
import os


# Grab the file path of our data
file_path = 'Resources/budget_data.csv'

budget_data = []

# total months
with open(file_path) as csvfile:

    reader= csv.DictReader(csvfile)

    for row in reader:
        budget_data.append({'month': row['Date'], 'amount': int(row['Profit/Losses']), 'change': 0})

# calculate total months
    months= len(budget_data)
    print('Total Months : ', months)

    prior = budget_data[0]['amount']
    for each in range(months):
        budget_data[each]['change'] = budget_data[each]['amount'] - prior
        total_change = sum(row['amount'] for row in budget_data)
    
    Average_change = total_change/months
    


    
# total profit/loss
with open(file_path) as csvfile:
    next(csvfile)
    total = sum(int(r[1]) for r in csv.reader(csvfile))
    print('total: ', total)

print('Average change : ', Average_change)

increase = max(budget_data, key=lambda x:x['change'])
decrease = min(budget_data, key=lambda x:x['change'])       
print('Greatest Increase in Profits :' , increase)
print('Greatest decrease in Profits :', decrease)


# Printting  the Final analysis and exporting to a text file 
# Set path for file
filepath = os.path.join('.', 'Resources', 'PyBank_Results.txt')
with open(filepath, "w") as text_file:
    print('Financial Analysis', file=text_file)
    print('----------------------------', file=text_file)
    print('Total Months : ', months,file=text_file)
    print('total: ', total,file=text_file)
    print('Average change : ', Average_change,file=text_file)
    print('Greatest Increase in Profits :' , increase,file=text_file)
    print('Greatest decrease in Profits :', decrease,file=text_file)








    

 









    

    













    


