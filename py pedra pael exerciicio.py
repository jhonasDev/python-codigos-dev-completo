from random import randint
opcoes = ('pedra','papel','tesoura')
npc = randint(0,2)
print('''escolha:
[0]pedra
[1]papel
[2]tesoura ''')
voce = int(input('faça sua escolha? '))
print('npc jogou {}'.format(opcoes[npc]))
print('voce jogou {}'.format(opcoes[voce]))

if npc == 0:
  if voce == 0:
    print('empatou')
  elif voce == 1:
    print('voce venceu')
  elif voce == 2:
    print('voce perdeu')
  else:
    print('invalidado')

elif npc == 1:
  if voce == 0:
    print('voce perdeu')
  elif voce == 1:
    print('empatou')
  elif voce == 2:
    print('voce ganhou')
  else:
    print('invalidado')

elif npc == 2:
  if voce == 0:
    print('voce ganhou')
  elif voce == 1:
    print('voce perdeu')
  elif voce == 2:
    print('empatou')
  else:
    print("invalidado")