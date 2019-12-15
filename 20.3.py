s = input()
c = 0
for i in range(len(s)):
    if 96 < ord(s[i]) < 123:
        c += 1
print(c)
