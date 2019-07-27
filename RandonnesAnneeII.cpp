#include <bits/stdc++.h>
using namespace std;
int nbPersonnes, nbVelos, nbChoix, scoreMax, scoreBase;
bool can_match(int indPersonne, vector<int> graph[10001], int vMatches[], bool seen[]){
   for(int indVelo : graph[indPersonne]){
      if(!seen[indVelo]){
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
    scoreMax = 0;
      vector<int> graph[10001];
      bool seen[10001];
      int vMatches[10001];
      cin>>nbPersonnes>>nbVelos>>nbChoix;
      for(int indVelo = 0; indVelo < nbVelos; ++indVelo){
         seen[indVelo] = false;
         vMatches[indVelo] = -1;
      }
      for(int indChoix = 0; indChoix < nbChoix; ++indChoix){
         int a,b;
         cin>>a>>b;
         graph[a].push_back(b);
      }
      for(int indPersonne = 0; indPersonne < nbPersonnes; ++indPersonne){
         for(int indVelo = 0; indVelo < nbVelos; ++indVelo) seen[indVelo] = false;
         if(can_match(indPersonne, graph, vMatches, seen)) scoreMax+=1;
      }
      cout<<scoreMax;
}