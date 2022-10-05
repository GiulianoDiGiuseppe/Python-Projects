import wikipediaapi
import json
import matplotlib.pyplot as plt

def main(): 
	wiki_api = wikipediaapi.Wikipedia('en')

	# Definition months and range of years
	months = [ 'January', 'February','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	years= [item for item in range(1992,2022)]

	# Decision of extract data
	answer=input("do you want to extract another time the data of deaths?[Y/N]")
	if answer=='Y':
		data_json=extract_death(years,months,wiki_api)	

		path=r'Data/death_1992_2022.json'
		with open(path, 'w') as f:
			json.dump(data_json, f, indent=3)
	else:
		path=r'Data\death_1992_2022.json'
		with open(path, 'r') as f:
			data_json = json.load(f)

	# structure data_json['1992']['January']['31'][2]
	dic_max , max_age , dic_min , min_age ,total,analysis_age_month,analysis_age_year = analysis_age_death(years,months,data_json)
	
	#Save information
	path=r'Data\analysis_month_1992_2022.json'
	with open(path, 'w') as f:
		json.dump(analysis_age_month, f, indent=3)
	path=path=r'Data\analysis_year_1992_2022.json'
	with open(path, 'w') as f:
		json.dump(analysis_age_year, f, indent=3)

	total ,analysis_number_year ,analysis_number_month = analysis_number_death(years,months,analysis_age_month)
	show_avg_age(years,analysis_age_year)
	show_death_time(years,analysis_number_year,analysis_number_month)
	
	print(" END ")

def show_death_time(years,analysis_number_year,analysis_number_month):
	plt.plot(analysis_number_year.keys(),analysis_number_year.values())
	plt.suptitle('dead for year')
	plt.show()

	analysis_number={}
	# sorted dictionary
	for year in years:
		for i,k in analysis_number_month[str(year)].items():
			date=str(str(year)+i)[2:6]
			#print(i,k)
			analysis_number[date]=k

	plt.plot((analysis_number.keys()),analysis_number.values())
	plt.suptitle('death for month')
	plt.show()

def show_avg_age(years,analysis_age_year):
	age_total={}
	# calculate total age
	for year in years:
		for i in range(119):
			if str(i) not in age_total.keys():
				age_total[str(i)]=0
			if str(i) in analysis_age_year[str(year)].keys():
				age_total[str(i)]+=analysis_age_year[str(year)][str(i)]
	
	plt.plot(age_total.keys(),age_total.values())
	plt.suptitle('dead age for year')
	plt.show()

	person=0
	sum_age=0
	for i, k in age_total.items():
		person+=k
		sum_age+=k*int(i)
	avg_age=sum_age/person
	print("average age is : ",avg_age)


def analysis_number_death(years,months,analysis_month):
	total=0
	deaths_year_month={}
	deaths_year={}
	# Scroll all information
	for year in years:
		deaths_year_month[str(year)]={}
		deaths_year[str(year)]=0
		for month in months:
			deaths_year_month[str(year)][month]=0
			for i , k in analysis_month[str(year)][month].items():
				total+=k
				deaths_year_month[str(year)][month]+=k
			deaths_year[str(year)]+=deaths_year_month[str(year)][month]
	
	return total ,deaths_year ,deaths_year_month

# output min and max age of people and 
# # give the dictionaries with age in a specific month or year
def analysis_age_death(years,months,data_json):
	min_age=100
	max_age=0
	dic_max=[]
	dic_min=[]
	answer3=input("Do you want to see max/min an animal or tree? :[Y/N]")
	if answer3=='Y':
		enable=True
	else:
		enable=False
	analysis_month={}
	analysis_year={}
	total=0

	# scroll all person
	for year in years:
		analysis_month[str(year)]={}
		analysis_year[str(year)]={}
		for month in months:
			analysis_month[str(year)][month]={}
			death_month=data_json[str(year)][month]
			for day in range(len(death_month)):
				for person in death_month[str(day+1)]:
					total+=1
					# search min e max
					dic_max , max_age = max_age_people(person,max_age,dic_max,enable)
					dic_min , min_age = min_age_people(person,min_age,dic_min,enable)
					
					age=person['age']

					# populate dictionaries
					if str(age) not in (analysis_year[str(year)]):
						analysis_year[str(year)][str(age)]=1
					if str(age) in (analysis_month[str(year)][month]):
						cnt=int(analysis_month[str(year)][month][str(age)])+1
						analysis_month[str(year)][month][str(age)]=cnt
						analysis_year[str(year)][str(age)]=int(analysis_year[str(year)][str(age)])+1
					else:
						analysis_month[str(year)][month][str(age)]=1
	# Print information		
	for i in range(len(dic_max)):
		print(" Max age is ",max_age,"His/her name is :",dic_max[i]['name'])
		if len(dic_max[i].keys())>2:
			print(" he/she is :",dic_max[i]['info'])
	for i in range(len(dic_min)):
		print(" Min age is ",min_age,"His/her name is :",dic_min[i]['name'])
		if len(dic_min[i].keys())>2:
			print(" he/she is :",dic_min[i]['info'])

	print("the total dead people in dataset is :", total)
	return dic_max , max_age , dic_min , min_age ,total,analysis_month,analysis_year

# give a person/people with themaximum age
def max_age_people(person,max_age,dic_max,enable):
	if person['age']==max_age :
		dic_max.append(person)
	elif person['age']>max_age and int(person['age'])<1894 and (int(person['age'])<122 or enable): 
		max_age=person['age']
		dic_max=[]
		dic_max.append(person)
	return dic_max , max_age

# give a person/people with the minimum age
def min_age_people(person,min_age,dic_min,enable):
	if int(person['age'])==min_age and (person['name']=='Paddles' or enable) :
		dic_min.append(person)
	elif person['age']<min_age and (person['name']=='Paddles' or enable):
		min_age=person['age']
		dic_min=[]
		dic_min.append(person)
	return dic_min , min_age


#extract dictionaries of deaths
def extract_death(years,months,wiki):
	dic_person={}
	# select all years and months
	for year in years:
		dic_person[str(year)]={}
		for month in months:
			print(year , month)
			# check and extract the deaths in a months
			page='Deaths_in_'+month+"_"+str(year)
			text=(check_pages(page,wiki)).text
			dic_person[str(year)][month]=parse_page(text)
	return dic_person

# give array with index-1 is day and value is people deaths
def parse_page(page):
	day_to_death={}
	people=[]
	cnt_day=1
	text = page.split("\n")
	enable=False #start to take data

	for line in text:
		if line==str(cnt_day):#take a new day
			day_to_death[str(cnt_day)]={}
			cnt_day+=1
			enable=True #enable line
		elif line!="" and line!=None and enable==True and not line.startswith("="): # extract person
			person=parse_line(line)
			if person!="" and person!=None:
				people.append(person)
		if line==None or line=="" and enable==True:# pass value in dictionary
			day_to_death[str(cnt_day-1)]=people
			people=[]
			enable=False

	return day_to_death

# return a set of people a dictionary with 3 keys (name,age,info)
def parse_line(line):
	person={}
	line_split=line.split(",")
    #Save lines like a dictionary considering different cases
	if line_split[0]=='=':
		return None
	if len(line_split)>1 :
		person["name"]=line_split[0]
		try:
			if len(line_split[1])>2:
				person["age"]=int(line_split[1])
			else:
				person["age"]=int((line_split[1][0:2]))
		except ValueError as e: # menage the error 
			return None
		if len(line_split)>3:
			person["info"]=line_split[2:]
		return person


#chek pages and return the link
def check_pages(page,wiki):
	return wiki.page(page)
	# TODO implement exception...
	

if __name__ == "__main__":
    main()



