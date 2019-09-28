
def get_max(length, somme):
	fs = ""

	for x in range(length):
		temp = min(9,somme) #On déborde pas , c'est pratique xd
		somme -= temp
		fs += str(temp)
	return fs
def get_min(length,somme):
	cur = ["1"]*length
	curSomme = length

	p = length-1

	while curSomme < somme and p >=0:
		if cur[p] == "9":
			p-=1
		else:
			cur[p] = str(int(cur[p])+1)
			curSomme += 1
	fchar = ""
	for item in cur:
		fchar += item
	return fchar



def main():
	m,s = map(int,input().split())
	if m == 1 and s == 0:
		print(0,0)
		return
	if m > s:
		print(-1,-1)
		return
	ml = get_max(m,s)
	minl = get_min(m,s)
	print(minl,ml)
main()