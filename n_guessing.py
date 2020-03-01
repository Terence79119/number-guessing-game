import random

r = random.randint(1, 100)
r = int(r)
x = 1
while True:
	ipt = input('請輸入一個數字: ')
	ipt = int(ipt)
	if ipt == r:
		print('你答對了!')
		break
	elif ipt > r:
		print('你輸入的數字比答案大喔')
		x = x + 1
	elif ipt < r:
		print('你輸入的數字比答案小喔')
		x = x + 1
	print('你總共猜了', x ,'次')
