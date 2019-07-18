ramenMap = {'NTU': (0, 0), 'Home': (-12.6, 21.3), 'Soba Shin': (2.6, 4.9), 'Itto': (-8.1, 10.3), 'GoNoKami': (6.7, 6.7), '山嵐': (-0.4, -0.3)}

f = input('From: ')
t = input('To: ')

print((ramenMap[t][0] - ramenMap[f][0], ramenMap[t][1] - ramenMap[f][1]))
