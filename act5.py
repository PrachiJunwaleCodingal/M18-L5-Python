#Designer Doormat
r = int(input("enter number of rows: "))
c= int(input("enter number of columns: "))
for i in range(1, r, 2): 
    print((i * ".|.").center(c,"-")) 
print("DOORMAT".center(c, "-"))
for i in range(r-2, -1, -2):
    print((i * ".|.").center(c, "-"))    