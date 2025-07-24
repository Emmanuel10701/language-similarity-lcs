def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [["" for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i+1][j+1] = dp[i][j] + X[i]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)

    return dp[m][n]

kamba = "miti ino muonza nene"
kikuyu = "ino miti mugwanja minene"

lcs_result = lcs(kamba, kikuyu)
print("LCS:", lcs_result)
print("LCS Length:", len(lcs_result))