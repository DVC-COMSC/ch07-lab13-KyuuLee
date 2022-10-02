numbers = [    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
               [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

cnt = 0
for i in range(1, len(numbers)-1):
	for j in range(1, len(numbers[0])-1):
		if numbers[i][j] and numbers[i+1][j] and numbers[i-1][j] and numbers[i][j-1] and numbers[i][j+1]:
			cnt += 1

print(cnt)

