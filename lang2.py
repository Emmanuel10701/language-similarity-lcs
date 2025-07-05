def longest_common_subsequence(sentence1, sentence2):
 
    m = len(sentence1)
    n = len(sentence2)

    # Create a 2D DP table to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if sentence1[i - 1] == sentence2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS string
    lcs_length = dp[m][n]
    lcs_string = [""] * lcs_length
    
    i = m
    j = n
    k = lcs_length - 1

    while i > 0 and j > 0:
        if sentence1[i - 1] == sentence2[j - 1]:
            lcs_string[k] = sentence1[i - 1]
            i -= 1
            j -= 1
            k -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    return "".join(lcs_string), lcs_length

if __name__ == "__main__":
    print("LCS Program for Linguistic Similarity")
    print("-" * 40)


    sentence_kamba = input("Enter the Kamba sentence: ").strip()
    sentence_kikuyu = input("Enter the Kikuyu sentence: ").strip()

    lcs, length = longest_common_subsequence(sentence_kamba, sentence_kikuyu)

    print("\n--- Results ---")
    print(f"Sentence 1 (Kamba): '{sentence_kamba}'")
    print(f"Sentence 2 (Kikuyu): '{sentence_kikuyu}'")
    print(f"Longest Common Subsequence (LCS): '{lcs}'")
    print(f"Length of LCS: {length}")