n = int(input('enter a number:'))
f = 1
 
for i in range(1, n+1):
    f = f*i

r = ('{:,}'.format(f))
print(str(r))

