def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [["" for _ in range(n+1)] for _ in range(m+1)]

    # Fill DP table
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + s1[i]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)

    return dp[m][n]

# Example usage
kamba = "miti mikulu musamvu ino"
kikuyu = "miti mikuru igĩtũgũ ino"

result = lcs(kamba, kikuyu)
print("LCS:", repr(result))
print("LCS Length:", len(result))
