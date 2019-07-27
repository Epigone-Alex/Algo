

def main():
	nbGuides, nbIntervalles = map(int,input().split())
	evenements = []

	for indIntervalle in range(nbIntervalles):
		deb, fin = map(int,input().split())
		evenements.append((deb, 1))
		evenements.append((fin, -1))
	evenements.sort(key = lambda x : x[0])

	for evenement in evenements:
		if evenement[1] == 1:
			if nbGuides == 0:
				print(0)
				return
			nbGuides -= 1
		elif evenement[1] == -1:
			nbGuides += 1
	print(1)
main()