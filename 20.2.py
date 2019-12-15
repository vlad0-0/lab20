s = list(input())
for i in range (len(s)):
    s.insert(2*i, " ")
del(s[0])
print("".join(s))
