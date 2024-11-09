import sys
input = sys.stdin.readline

n = int(input())
cat = 1
cnt=0

if n == 0 or n == 1:
	cnt = n
	print(cnt)
else:
	while cat!= n:
		if cat >= n-cat:
			cat += n-cat
			cnt +=1 
		else:
			cat = cat*2
			cnt += 1
	print(cnt+1)