import random

r = random.randint(1, 100)
r = int(r)

while True:
	ipt = input('請輸入一個數字: ')
	ipt = int(ipt)
	if ipt == r:
		print('你答對了!')
		break
	else:
		if ipt > r:
			print('你輸入的數字比答案大喔')
		else:
			print('你輸入的數字比答案小喔')

