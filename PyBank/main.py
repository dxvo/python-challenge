import csv

file = "budget_data.csv"
with open(file, newline = '') as inputFile:
	try:
		file_obj = csv.reader(inputFile, delimiter = ',')
		next(file_obj)
		#declaring variables 
		month = 0
		total = 0
		greatest_increase = 0
		greatest_decrease = 0
		arr = ["",""] #result[0] for greast_increase
		data = []
		monthly = []
		total_change = 0


		for row in file_obj:
			total += int(row[1])
			month += 1
			data.append(row)



		for i in range(1,len(data)):
			change= int(data[i][1]) - int(data[i-1][1])
			monthly.append(change)
			total_change += change


			if(change > greatest_increase):
				greatest_increase = change
				arr[0] = data[i][0]
			elif (change  < greatest_decrease):
				greatest_decrease = change
				arr[1] = data[i][0]

		avg_change =round(total_change/(month - 1),2)
				
	finally:
		inputFile.close()
print()
print("\n---------FINANCIAL ANALYSIS---------")
print("Total month: ",month)
print("Total: ","$"+ str(total))
print("Avg Change: ","$" + str(avg_change))
print("Greatest Increase in Profits: ",arr[0],"($" + str(greatest_increase)+ ")")
print("Greatest Decrease in Profits: ",arr[1],"($" + str(greatest_decrease)+ ")")


with open("PyBank_out.txt",'w') as outFile:
	try:
		outFile.write("\n---------FINANCIAL ANALYSIS---------\n")
		outFile.write("Total month: " + str(month)+ "\n")
		outFile.write("Total: "+ "$"+ str(total)+"\n")
		outFile.write("Avg Change: "+"$" + str(avg_change)+"\n")
		outFile.write("Greatest Increase in Profits: " + str(arr[0])+" " +"($" + str(greatest_increase)+ ")"+"\n")
		outFile.write("Greatest Decrease in Profits: " + str(arr[1])+ " " + "($" + str(greatest_decrease)+ ")"+"\n")
	finally:
		outFile.close()






