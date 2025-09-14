def longest_common_substring(str1: str, str2: str) -> str:
    """
    LCS!
    """

    # constants
    n = len(str1)
    m = len(str2)

    # create an empty dp
    dp = [[None for _ in range(n+1)] for b in range(m+1)]

    # initialize the dp
    dp[0] = [0 for _ in range(n+1)]
    for arr in dp:
        arr[0] = 0


    for j in range(1, m+1):
        for i in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[j][i] = dp[j-1][i-1] + 1
            else:
                dp[j][i] = max(dp[j-1][i], dp[j][i-1])

    return dp[m][n]
