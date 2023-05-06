# тестовый файл для практики работы с GIT
# функция с элемпентами модуля random

import random
def cubs_game():
  total_attemps = 5 # число попыток в одном раунде
  comp_point = 0
  player_point = 0

  while total_attemps > 0:
    comp_attemp = random.randint(1, 6)
    print(f'Бросаем кости...\nБросок...\nКУБ КОМПЬЮТЕРА: {comp_attemp}')

    input('Нажмите ENTER для броска: ')
    player_attemp = random.randint(1, 6)
    print(f'КУБ ИГРОКА: {player_attemp}')

    if comp_attemp > player_attemp:
      print('Ты проиграл!\n')
      comp_point += 1
    elif comp_attemp < player_attemp:
      print('Ты победил!\n')
      player_point += 1
    else:
      print('Ничья!\n')
      comp_point += 1
      player_point += 1

    print(f'    ТЕКУЩИЙ СЧЁТ')
    print('=====================')
    print(f'ИГРОК - {player_point} : {comp_point} - КОМП\n')

    total_attemps -= 1
  print(f'    ИТОГОВЫЙ СЧЕТ')
  print('=====================')
  print(f'ИГРОК - {player_point} : {comp_point} - КОМП\n')

cubs_game()
