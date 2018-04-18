import csv

data = []
with open('City_Budget_Expenditures.csv', newline='') as file:
	reader = csv.reader(file,dialect='excel')
	for row in reader:
		data.append(row)

used = set()
data_no_dups = []
for i in range(1,len(data)):
	year = data[i][0]
	dept = data[i][1]
	check = (year,dept)
	if check not in used:
		s = int(round(float(data[i][2].strip('$').replace(',','').strip())*100))
		for j in range(i+1,len(data)):
			year2 = data[j][0]
			dept2 = data[j][1]
			if year == year2 and dept == dept2:
				s += int(round(float(data[j][2].strip('$').replace(',','').strip())*100))
		data_no_dups.append([year,dept,s])
		used.add(check)

data_long = []
used = set()
for i in data_no_dups:
	department_name = i[1]
	if department_name not in used:
		data_2012 = 0
		data_2013 = 0
		data_2014 = 0
		data_2015 = 0
		data_2016 = 0
		data_2017 = 0
		data_2018 = 0
		for j in data_no_dups:
			if(j[1]==department_name):
				year = int(j[0])
				if year == 2012:
					data_2012 = j[2]
				elif year == 2013:
					data_2013 = j[2]
				elif year == 2014:
					data_2014 = j[2]
				elif year == 2015:
					data_2015 = j[2]
				elif year == 2016:
					data_2016 = j[2]
				elif year == 2017:
					data_2017 = j[2]
				elif year == 2018:
					data_2018 = j[2]
		used.add(department_name)
		data_long.append([department_name,
						  data_2012,
						  data_2013,
						  data_2014,
						  data_2015,
						  data_2016,
						  data_2017,
						  data_2018])

data_long.sort()
final_data = [["Department",
			   "2012",
			   "2013",
			   "2014",
			   "2015",
			   "2016",
			   "2017",
			   "2018"]]
for i in data_long:
	final_data.append(i)

with open("budget.csv","w+",newline='') as file:
	writer = csv.writer(file,dialect='excel')
	for i in final_data:
		writer.writerow(i)