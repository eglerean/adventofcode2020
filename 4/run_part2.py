import re
filepath='input.txt'

# load the input and store it as numpy matrix of 0 (free) and 1 (tree)
cnt = 0
records=[];
with open(filepath) as fp:
	record={};
	for line in fp:
		line = line.strip()
		print(line)
		if len(line) == 0:
			records.append(record)
			# new record
			record={}

		regex = r'\w+:#*?\w+'
		list1=re.findall(regex,line)
		for n in list1:
			temp=n.split(':')
			if temp[0] != 'cid':
				record[temp[0]]=temp[1];


	records.append(record)

def check_years(year,min_year,max_year):
	if len(year) < 4 :
		return 0

	if int(year) < min_year :
		return 0

	if int(year) > max_year :
		return 0

	return 1


def check_height(hgt):
	if hgt[-2:] == "cm":
		num = int(re.sub('[^0-9]','', hgt))
		if 150 <= num <= 193:
			return 1

	if hgt[-2:] == "in":
		num = int(re.sub('[^0-9]','', hgt))
		if 59 <= num <= 76:
			return 1

	return 0


print("-----")

numval=0
for r in records:
	print(r)
	if(len(r) < 7):
		print('Not valid length')
		continue
	
	if check_years(r['byr'],1920,2002) == 0:
		print('Not valid byr')
		continue
	
	if check_years(r['iyr'],2010,2020) == 0:
		print('Not valid iyr')
		continue

	if check_years(r['eyr'],2020,2030) == 0:
		print('Not valid eyr')
		continue

	if check_height(r['hgt']) == 0:
		print('Not valid hgt')
		continue

	match_hex_col = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', r['hcl'])
	if match_hex_col:
		print('Valid hair col')
	else:
		print('Not valid hair col')
		continue

	listOfEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] 
	if r['ecl'] in listOfEyeColors:
		print('Valid eye col')
	else:
		print('Not valid eye col')
		continue

	pid=re.sub('[^0-9]','', r['pid'])

	if len(pid) != 9:
		print("Not valid pid")
		continue

	# if you reach this place it is valid
	numval += 1


print(numval)		

		
