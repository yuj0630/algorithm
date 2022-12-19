#32. 정수 삼각형
n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split)))
    #다이나믹 프로그래밍으로 두 번째 줄부터 내려가면서 확인
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                up_left = 0
            else:
                up_left = dp[i - 1][j - 1]
            #바로 위에서 내려오는 경우
            if j == i:
                up = 0
            else:
                up = dp[i - 1][j]
            dp[i][j] = dp[i][j] + max(up_left, up)
    print(max(dp[n-1]))
