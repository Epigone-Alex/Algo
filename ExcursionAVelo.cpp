#include <bits/stdc++.h>
using namespace std;
int nbPersonnes, nbVelos, nbChoix, scoreMax, scoreBase;
bool can_match(int indPersonne, bool graph[1001][1001], int vMatches[], bool seen[]){
   for(int indVelo = 0; indVelo < nbVelos; ++indVelo){
      if(graph[indPersonne][indVelo] && !seen[indVelo]){
         seen[indVelo] = true;
         if(vMatches[indVelo] == -1 || can_match(vMatches[indVelo], graph, vMatches, seen)){
            vMatches[indVelo] = indPersonne;
            return true;
         }
      }
   }
   return false;
}
int main()
{
   ios::sync_with_stdio(false);
    cin.tie(0);
    scoreBase = 0;
    scoreMax = 0;
      bool graph[1001][1001];
      bool seen[1001];
      int vMatches[1001];
      cin>>nbPersonnes>>nbVelos>>nbChoix;
      for(int indPersonne = 0; indPersonne < nbPersonnes; ++indPersonne)
         for(int indVelo = 0; indVelo < nbVelos; ++indVelo)
            graph[indPersonne][indVelo] = false;
      for(int indVelo = 0; indVelo < nbVelos; ++indVelo){
         seen[indVelo] = false;
         vMatches[indVelo] = -1;
      }
      for(int indChoix = 0; indChoix < nbChoix; ++indChoix){
         int a,b,c;
         cin>>a>>b>>c;
         graph[a][b] = true;
         scoreBase += c;
      }
      for(int indPersonne = 0; indPersonne < nbPersonnes; ++indPersonne){
         for(int indVelo = 0; indVelo < nbVelos; ++indVelo) seen[indVelo] = false;
         if(can_match(indPersonne, graph, vMatches, seen)) scoreMax+=1;
      }
      if(scoreMax == scoreBase) cout<<"OUI";
      else cout<<"NON";
}
