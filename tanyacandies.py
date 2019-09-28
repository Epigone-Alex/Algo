

def main():
	nbCandies = int(input())
	candTab = list(map(int,input().split()))

	pairSomme = 0
	impairSomme = 0

	for indCandy,candy in enumerate(candTab):
		if indCandy%2 == 0: pairSomme += candy
		else: impairSomme += candy

	curpSomme = 0
	curimpSomme = 0
	nbGoods = 0

	for indCandy, candy in enumerate(candTab):
		if indCandy%2 == 0: pairSomme -= candy
		else: impairSomme -= candy
		#print(pairSomme,impairSomme,curpSomme,curimpSomme)
		#if pairSomme == impairSomme and curimpSomme == curpSomme:
		if pairSomme+curimpSomme==impairSomme+curpSomme:
			nbGoods += 1

		if indCandy%2 == 0: curpSomme += candy
		else: curimpSomme += candy
	"""YES JOUBLIAIS DE PRINT IOUGAQSDMKLhsmfojkqshgdfmoqishdfù oqsidufmowdiuytfhsqwmodifusqklk
	sfdsdfsd
	fsd
	fs
	df
	s"""

	print(nbGoods)
main()