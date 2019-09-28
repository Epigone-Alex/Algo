task_name = "ride"


"""
ID: alexand185
LANG: PYTHON3
TASK: ride
"""
fin = open ('{}.in'.format(task_name), 'r')
fout = open ('{}.out'.format(task_name), 'w')
input = fin.readline
first = input()
nba = 1
for char in first: nba *= ord(char)-64
second = input()
nbb = 1
for char in second: nbb *= ord(char)-64

if nba%47 == nbb%47:
	fout.write("GO")
else:
	fout.write("STAY")

fout.write("\n")


fout.close()