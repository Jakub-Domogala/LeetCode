r = {'i':1, 'al':2, 'ale':3}
s = 'iale'
for i in range(len(s)):
    if s[i:i+2] in r:
        print(i, s[i:i+2])