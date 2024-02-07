n = int(input())
c = -1
for i in range(1,len(str(n))+1):
    if i!=len(str(n)):
        c+=i*(10**(i)-10**(i-1))
    else:
        c+=(n-10**(i-1)+1)*i
a = "1"
print(" "*c+a)
for j in range(n-1,0,-1):
    a = str((int(a[-len(str(n - j))::]) + 1)) + a + str((int(a[-len(str(n - j))::]) + 1))
    c = c - len(str(n-j+1))
    print(" " * c + a)