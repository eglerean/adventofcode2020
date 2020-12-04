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


numval=0
for r in records:
	if(len(r) < 7):
		print('not valid')
	else:
		print('valid')
		numval += 1

print(numval)
		
