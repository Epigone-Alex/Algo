
#include <bits/stdc++.h>
using namespace std;


int main()
{
	long long minP = 1000*1000*1000;
	int nbCases;
	cin>>nbCases;

	if(nbCases == 1) cout<<4<<endl;
	else {
		int a = sqrt(nbCases);
		int b = nbCases/a;
		nbCases%=(a*b);
		if(nbCases != 0) nbCases = 2;
		cout<<2*a+2*b+nbCases<<endl;
	}
	return 0;
}