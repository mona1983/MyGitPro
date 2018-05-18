l=[]
def printFun(l):
	print('Print values')
	for i in range(3):
		for j in range(3):
			print(l[i][j],end=' ')
		print('\n')
def swapFun(favChar,favNumber,l):
	for i in range(3):
		sub_list=l[i]
		print(sub_list)
		if favNumber in sub_list:
			l[i][sub_list.index(favNumber)] = favChar
def Decision(l,player):
	isWon=0
	if (l[0][0] == player) & (l[1][0] == player ) & (l[2][0] == player):
		isWon=1
	elif (l[0][1] == player) & (l[1][1] == player )& (l[2][1] == player):
		isWon=1
	elif (l[0][2] == player) & (l[1][2] == player )& (l[2][2] == player):
		isWon=1
	elif (l[0][0] == player) & (l[0][1] == player ) & (l[0][2] == player):
		isWon=1
	elif (l[1][0] == player) & (l[1][1] == player ) & (l[2][1] == player):
		isWon=1
	elif (l[2][0] == player) & (l[2][1] == player ) & (l[2][2] == player):
		isWon=1
	elif (l[0][0] == player) & (l[1][1] == player ) & (l[2][2] == player):
		isWon=1
	elif (l[0][2] == player) & (l[1][1] == player ) & (l[2][0] == player):
		isWon=1
	else:
		print('Decision')
		return 0
	if player =='O':
		if isWon==1:
			print('Player 1 Own the match *********************Game Over')
			return 1
	if player =='X':
		if isWon== 1:
			print('Player 2 Own the match *********************Game Over')
			return 1
row_len=3
col_len=3
for i in range(row_len):
	l.append([0]*row_len)
	for j in range(row_len):
		l[i][j]=int(input("Enter the value for ist"))

printFun(l)
print(l)
i=2
isContinue=0
for i in range(row_len):
	for j in range(row_len):
		#int(input("Enter the value for ist"))
		if i%2==0:
			swapFun('O',int(input("Player 1 Enter You favorite number")),l)
			printFun(l)
			isContinue=Decision(l,'O')
		if i%2==1:
			swapFun('X',int(input("Player 2 Enter You favorite number")),l)
			printFun(l)
			isContinue=Decision(l,'X')
		i+=1
		if isContinue==1:
			break
	if isContinue==1:
		break
print(l)