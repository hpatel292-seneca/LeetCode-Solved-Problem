s="nfpdmpi"
 
i=0
j=0
maxLength=0
for index in range(1, len(s)):
    subString = s[i:j+1]
    if s[index] in subString:
        i=i+subString.index(s[index])+1
        j=j+1
        if j-i+1 > maxLength:
            maxLength=j-i+1
    else:
        j=j+1
        maxLength=j-i+1

print(maxLength)

# Solution beats 93.36% on leetcode.