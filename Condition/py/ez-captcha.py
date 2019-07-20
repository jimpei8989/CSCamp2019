secret = 'howhow'
captcha = input('Please input the characters in the bracket "{}"\n>'.format(secret))

if secret == captcha:
	print('Valid User')

if secret != captcha:
	print('Invalid User')