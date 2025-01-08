#Mirrored Triangle

r = int(input("Enter Number of Rows:"))
for i in range(1,r+1):
    for j in range(1,r+1):
        if(j <= r - i):
            print(' ', end = '  ')
        else:
            print('$', end = '  ')
    print()