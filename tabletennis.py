

def main():
	n,k = map(int,input().split())
	tabT = list(map(int,input().split()))
	if k > n:
		print(max(tabT))
	else:
		won = [0]*n
		q = [x for x in range(n)]
		while  won[q[0]] < k:
			t1 = tabT[q[0]]
			t2 = tabT[q[1]]
			if t1 > t2:
				won[q[0]] += 1
				q.append(q.pop(1))
			else:
				won[q[1]] += 1
				q.append(q.pop(0))
		print(tabT[q[0]])
main()
