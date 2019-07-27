import sys
input = sys.stdin.readline
def main():
   monIdent = int(input())  
   nbRelations = int(input())
   nb = 0
   relations = [[] for x in range(65000)]
   amisTraites = [False for x in range(65000)]
   for indRelation in range(nbRelations):
      a,b = map(int,input().split())
   
      relations[a].append(b)
      relations[b].append(a)
   amisTraites[monIdent] = True
   for amis in relations[monIdent]: amisTraites[amis] = True
   for amisD in relations[monIdent]:
      for amisND in relations[amisD]:
         if not amisTraites[amisND]:
            amisTraites[amisND] = True
            nb += 1
   print(nb)
main()