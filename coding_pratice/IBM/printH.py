n = 10
th = int()
if n%2!=0:
    th = n
c = 'H'
for i in range(th):
    uc = (i*2+1)*c
    wdt = th*2-1
    print(uc.center(wdt))
for _ in range(th+1):
    print((c*th).center(th*2) + (c*th).center(th*6))
for _ in range((th+1)//2):
    print((c*th*5).center(th*6))
for _ in range(th+1):
    print((c*th).center(th*2) + (c*th).center(th*6))
for i in range(th, 0, -1):
    uc = (i*2-1)*c
    wdt = th*5*2


