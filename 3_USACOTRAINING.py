task_name = "gift1"


"""
ID: alexand185
LANG: PYTHON3
TASK: gift1
"""
fin = open ('{}.in'.format(task_name), 'r')
fout = open ('{}.out'.format(task_name), 'w')
input = fin.readline
dic = {}
n = int(input())

for x in range(n):
	dic[input().replace("\n","")] = 0
dic
for x in range(n):
	giver = input().replace("\n","")
	amount, nb = map(int,input().split())
	if nb > 0:
		to_give = amount//nb
		dic[giver] += amount%nb
		dic[giver] -= amount
		for y in range(nb):
			dic[input().replace("\n","")] += to_give
for item in dic:
	fout.write(item + " " + str(dic[item]) + "\n")

fout.close()