#include <bits/stdc++.h>
using namespace std;
int nbInter, nbVertex,numberApp;
vector<bool> visited;
vector<int> appTab;
vector<int> transGraph[1001];
vector<int> finalApp;
vector<int> graph[1001];
void dfs(int curVertex)
{
   if(!visited[curVertex])
   {
      visited[curVertex] = true;
      for(int neiVertex : graph[curVertex])
      {
         dfs(neiVertex);
         transGraph[neiVertex].push_back(curVertex);
      }
      numberApp--;
      appTab[numberApp] = curVertex;
   }
}
void assign(int curVertex, int rootVertex)
{
   if(visited[curVertex])
   {
      visited[curVertex] = false;
      finalApp[curVertex] = rootVertex;
      for(int neiVertex : transGraph[curVertex])
      {
         assign(neiVertex, rootVertex);
      }
   }
}
int main()
{
   ios::sync_with_stdio(false);
   cin.tie(0);
   cin>>nbInter>>nbVertex;
   visited.resize(nbInter, false);
   appTab.resize(nbInter, 0);
   finalApp.resize(nbInter, 0);
   numberApp = nbInter;
   for(int indVertex; indVertex < nbVertex ; ++indVertex){
      int dep,arr;
      cin>>dep>>arr;
      dep--;arr--;
      graph[dep].push_back(arr);
   }
   for(int indInter; indInter < nbInter; ++indInter) dfs(indInter);
   for(int curInter : appTab) assign(curInter, curInter);
   //for(int item : finalApp) cout<<item<<endl;
   vector<int> seen(nbInter, 0);
   int diffCounter = 0;
   for(int item : finalApp)
   {
      if(!seen[item]){
         seen[item] = 1;
         diffCounter++;
      }
   }
   cout<<diffCounter;
   return 0;
}