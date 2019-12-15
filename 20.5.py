s = input()
s0 = input()
c = 0
if len(s0) > len(s):
    print(c)
else:
    for i in range(len(s)-len(s0)+1):
        if s[i:i+len(s0)] == s0[:]:
            c += 1
print(c)
