# Time Complexity:   O(n+m)
# Memory Complexity: O(n+result)

def KMPSearch(pat, txt):
    def computeLPSArray(pat):
        M = len(pat)
        lps = [0] * M
        length = 0
        i = 1
        while i < M:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return lps

    M = len(pat)
    N = len(txt)
    lps = computeLPSArray(pat)
    result = []
    i = 0  # index for txt
    j = 0  # index for pat
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            j += 1
            i += 1
        if j == M:
            result.append(i - j)
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result


txt = "aaaa"
pat = "aaa"
result = KMPSearch(pat, txt)
print(result)
