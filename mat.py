def main():
    nbLig,nbCol = map(int,input().split())
    
    candTab = [input() for indLig in range(nbLig)]
    dset = set()
    for indLig in range(nbLig):
        dwarf = -1
        candy = -1
        for indCol in range(nbCol):
            if candTab[indLig][indCol] == "G":
                dwarf = indCol
            elif candTab[indLig][indCol] == "S":
                candy = indCol
                break
        if dwarf == -1:
            return -1
        dset.add(candy-dwarf)
    return len(dset)
print(main())