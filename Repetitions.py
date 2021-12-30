n = list(input())

c = 0
m = 0

for i in range(len(n)-1):
    if n[i] == n[i+1]:
        c = c +1
        if m < c:
            m = c
    
    elif n[i] != n[i+1]:
        c = 0

print(m+1)