#include <bits/stdc++.h>
using namespace std;
int nbBatons, longueurBaton, colonneBaton, maxHauteur = 0;
char typeBaton;
vector<int> plateauJeu(100,0);
void deplacementHorizontal()
{
    int curMax = 0;
    for(int indCol = colonneBaton; indCol < colonneBaton + longueurBaton; ++indCol) curMax = max(curMax, plateauJeu[indCol]);
    for(int indCol = colonneBaton; indCol < colonneBaton + longueurBaton; ++indCol) plateauJeu[indCol] = curMax + 1;
}
void deplacementVertical()
{
   plateauJeu[colonneBaton] += longueurBaton;
}
int main()
{
   ios::sync_with_stdio(false);
    cin.tie(0);
    cin>>nbBatons;
    for(int indBaton = 0; indBaton < nbBatons; ++indBaton) {
      cin>>typeBaton>>longueurBaton>>colonneBaton;
      if(typeBaton == 'V') deplacementVertical();
      else deplacementHorizontal();
    }
    for(int indCol = 0; indCol < 100; ++indCol) maxHauteur = max(maxHauteur, plateauJeu[indCol]);
    cout<<maxHauteur;
   return 0;
}