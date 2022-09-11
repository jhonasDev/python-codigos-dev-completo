from random import randint
opcoes = ('pedra','papel','tesoura')
npc = randint(0,2)
print('''escolha:
[1]pedra
[2]papel
[3]tesoura ''')
voce = int(input('faça sua escolha? '))
print('npc jogou {}'.format(opcoes[npc]))
print('voce jogou{}'.format(opcoes[voce]))