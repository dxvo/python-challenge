import csv

class candidate():
	def __init__(self,name,vote):
		self.name = name
		self.vote = vote


file = "election_data.csv"
with open(file, newline = '') as inputFile:
	try:
		file_obj = csv.reader(inputFile, delimiter = ',')
		next(file_obj)

		candidate_set = set()
		data = []

		#Add name to set to avoid checking for duplicate
		for row in file_obj:
			candidate_set.add(row[2])
			data.append(row)

		total_vote = len(data)
		num_of_candidate = len(candidate_set)
		candidate_list = []

		#Add candidate to list 
		for name in candidate_set:
			candidate_list.append(candidate(name,0))

		for i in range(len(data)):
			name = data[i][2]
			for j in range(num_of_candidate):
				if(candidate_list[j].name == name):
					candidate_list[j].vote += 1

	finally:
		inputFile.close()


for x in candidate_list:
	print(x.name, x.vote)