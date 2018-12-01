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
		arr = ["",""]

		for row in file_obj:
			total += int(row[1])
			month += 1
			curr_value = int(row[1])

			if(curr_value > greatest_increase):
				greatest_increase = curr_value
				arr[0] = row
			elif (curr_value  < greatest_decrease):
				greatest_decrease = curr_value
				arr[1] = row
	finally:
		inputFile.close()

print("\n---------FINANCIAL ANALYSIS---------")
print("Total month: ",month)
print("Total: ","$"+ str(total))
print("Avg Change: ","$" + str(round(total/month,2)))
print("Greatest Increase in Profits: ",arr[0][0],"($" + str(arr[0][1])+ ")")
print("Greatest Decrease in Profits: ",arr[1][0],"($" + str(arr[1][1])+ ")")


with open("PyBank_out.txt",'w') as outFile:
	try:
		outFile.write("\n---------FINANCIAL ANALYSIS---------\n")
		outFile.write("Total month: " + str(month)+ "\n")
		outFile.write("Total: "+ "$"+ str(total)+"\n")
		outFile.write("Avg Change: "+"$" + str(round(total/month,2))+"\n")
		outFile.write("Greatest Increase in Profits: " + str(arr[0][0])+" " +"($" + str(arr[0][1])+ ")"+"\n")
		outFile.write("Greatest Decrease in Profits: " + str(arr[1][0])+ " " + "($" + str(arr[1][1])+ ")"+"\n")
	finally:
		outFile.close()






