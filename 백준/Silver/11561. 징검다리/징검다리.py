t = int(input())

for _ in range(t):
	n = int(input())
	start = 1
	end = n
	result = 0
	

	while start <= end:
	    mid = (start + end) // 2
	    if ((mid + 1) * mid) // 2 <= n:
	        start = mid + 1
	        result = mid
	    else:
	        end = mid - 1
	print(result)