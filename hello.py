def square(z):
	print("{}的平方是{}".format(z,z*z))

x = int(input("輸入一個數字"))
print("你輸入的是",x)

if (x<=0):
	print("輸入值小於0")
elif(x==0):
	print("等於0")
else:
	for i in range(1,x+1):
		square(i)