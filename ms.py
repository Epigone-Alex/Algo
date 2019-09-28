import time

def main():
	nbLig = int(input())
	nbColonnes = int(input())#nbLig
	t1 = time.perf_counter()

	#On initialise tout pour exécuter l'algo

	depl = [(0,1),(0,-1),(1,0),(-1,0)]
	entree = (-1,-1,False)
	sortie = (-1,-1,False)
	seen = [[0] * nbColonnes for x in range(nbLig)]

	for indLigne in range(nbLig):
		curLigne = input()
		for indCol, char in enumerate(curLigne):
			if char == "X":
				if not entree[2]:
					entree = (indLigne, indCol, True)
				else:
					sortie = (indLigne, indCol, True)
			elif char == "W" or char == "1":
				seen[indLigne][indCol] = 1

	tabProfondeur = [[1000000]*nbColonnes for x in range(nbLig)]

	#Le parcours en largeur

	entree = (entree[0], entree[1])
	sortie = (sortie[0], sortie[1])
	queue = [sortie]
	tabProfondeur[sortie[0]][sortie[1]] = 0
	while len(queue) > 0:
		curCase = queue.pop(0)
		for indNei in range(4):
			curx = curCase[0] + depl[indNei][0]
			cury = curCase[1] + depl[indNei][1]
			if curx < nbLig and cury < nbColonnes and curx >= 0 and cury >= 0 and not seen[curx][cury]:
				seen[curx][cury] = 1
				tabProfondeur[curx][cury] = min(tabProfondeur[curCase[0]][curCase[1]]+1, tabProfondeur[curx][cury]) #A vérifier en premier
				queue.append((curx,cury))

	#Un parcours d'arbre pour retracer tout le chemin

	curCase = entree
	chemin = [entree]
	while curCase != sortie:
		curMin = tabProfondeur[curCase[0]][curCase[1]]
		curMinInd = curCase
		for indNei in range(4):
			curx = curCase[0] + depl[indNei][0]
			cury = curCase[1] + depl[indNei][1]
			if curx < nbLig and cury < nbColonnes and curx >= 0 and cury >= 0 and tabProfondeur[curx][cury] < curMin:
				curMinInd = (curx,cury)
				curMin = tabProfondeur[curx][cury]
		chemin.append(curMinInd)
		curCase = curMinInd

	#On refait le labyrinthe mais avec le chemin cette fois

	tabSol = [["O"]*nbColonnes for x in range(nbLig)]
	for x in range(nbLig):
		for y in range(nbColonnes):
			if tabProfondeur[x][y] == 1000000:tabSol[x][y] = "W"
	t2 = time.perf_counter()
	for case in chemin:
		tabSol[case[0]][case[1]] = "."
	tabSol[entree[0]][entree[1]] = "X"
	tabSol[sortie[0]][sortie[1]] = "X"

	#On l'affiche

	for item in tabSol:
		for item2 in item:
			print(item2, end = " ")
		print() 
	print(f"Executed in {t2-t1} seconds")
main()


