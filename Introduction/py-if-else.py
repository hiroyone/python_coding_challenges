n = int(input())
if n % 2 == 1:
    print("Weird")
elif (n in range(2, 6)) & (n % 2 == 0):
    print("Not Weird")
elif (n in range(6, 21)) & (n % 2 == 0):
    print("Weird")
else:
    print("Not Weird")
