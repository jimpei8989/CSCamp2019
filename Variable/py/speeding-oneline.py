print('Output a: {}'.format(list(map(lambda t : ((50 / 3.6) ** 2 - (t[0] / 3.6) ** 2) / 2 / t[1], [(float(input('Input v: ')), float(input('Input d: ')))]))[0]))
