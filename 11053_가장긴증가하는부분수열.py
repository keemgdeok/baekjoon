N = int(input())
A = list(map(int, input().split()))

dp=[1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i]=max(dp[j]+1, dp[i])
print(dp)
print(max(dp))