boss_HP = int(input('Boss HP: '))

adverturer_ATK = int(input('Adventurer\'s ATK: '))
fatguy_ATK = int(input('Fat guy\'s ATK: '))
kenshi_ATK = int(input('Kenshi no ATK: '))

rounds = 0

while boss_HP > 0:
	boss_HP -= adverturer_ATK
	rounds += 1

	if boss_HP > 0:
		boss_HP -= fatguy_ATK
		rounds += 1
	
	if boss_HP > 0:
		boss_HP -= kenshi_ATK
		rounds += 1

	print('Round {}, boss remain {} HP'.format(rounds, boss_HP))

print(rounds)