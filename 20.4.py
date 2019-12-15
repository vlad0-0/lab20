c = ""
while len(c) > 1 or c == "":
    c = input()
s = list(input())
for i in range(len(s)):
    if s[i] == c:
        s[i] *= 2
print("".join(s))
