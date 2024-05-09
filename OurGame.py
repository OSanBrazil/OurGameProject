# Bibliotecas

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import keyboard
import random
from sys import exit

# Seta as variáveis
ScreenWidth = 1120
ScreenHeight = 664
playerpool_pos = (900, 260)
number_of_players = 0

fps_rate = 60
frame_counter = 0
key_delay = 0
game_paused = False
critical_animation = False

player_pos = [-1, -1, -1, -1]
player_initial_pos = [-1, -1, -1, -1]
current_player = 0
player_steps = -1
player_direction = 1
collision = False
steps_way = 0
step_counter = 0
arrowX = 0
arrowY = 0
inverse_arrow = 0
Y_fluctuation = 0
fluctuation_factor = .003
max_fluctuation = 6
diagonal_adjust = 42
knight_anim = 0
dice_isrolling = -1
bomb_isexploding = -1
scorpion_isstinging = -1
hole_isfalling = -1
chest_isopening = -1
player_isexitinghole = -1
card_isshowing = -1
card_taken = -1

player_won = -1
exploding_player = -1
stung_player = -1
falling_player = -1
prized_player = -1
dice_side = 0
game_isinmenu = 2
game_isinend = -1
debug_mode = False
help_mode = False

# Seta a tela o framerate e carrega as surperfícies de gráficos e os sons
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("MAGICAL ADVENTURE")
clock = pygame.time.Clock()

# Images:
background_surface = pygame.image.load('graphics/tabuleiro.png').convert()
knight_surface1_blue = pygame.image.load('graphics/knight1_blue.png').convert_alpha()
knight_surface2_blue = pygame.image.load('graphics/knight2_blue.png').convert_alpha()
knight_surface3_blue = pygame.image.load('graphics/knight3_blue.png').convert_alpha()
knight_surface1_red = pygame.image.load('graphics/knight1_red.png').convert_alpha()
knight_surface2_red = pygame.image.load('graphics/knight2_red.png').convert_alpha()
knight_surface3_red = pygame.image.load('graphics/knight3_red.png').convert_alpha()
knight_surface1_green = pygame.image.load('graphics/knight1_green.png').convert_alpha()
knight_surface2_green = pygame.image.load('graphics/knight2_green.png').convert_alpha()
knight_surface3_green = pygame.image.load('graphics/knight3_green.png').convert_alpha()
knight_surface1_yellow = pygame.image.load('graphics/knight1_yellow.png').convert_alpha()
knight_surface2_yellow = pygame.image.load('graphics/knight2_yellow.png').convert_alpha()
knight_surface3_yellow = pygame.image.load('graphics/knight3_yellow.png').convert_alpha()
dice_surface1 = pygame.image.load('graphics/dice1.png').convert_alpha()
dice_surface2 = pygame.image.load('graphics/dice2.png').convert_alpha()
dice_surface3 = pygame.image.load('graphics/dice3.png').convert_alpha()
dice_surface4 = pygame.image.load('graphics/dice4.png').convert_alpha()
dice_surface5 = pygame.image.load('graphics/dice5.png').convert_alpha()
dice_surface6 = pygame.image.load('graphics/dice6.png').convert_alpha()
arrow_surface = pygame.image.load('graphics/arrow1.png').convert_alpha()
bomb_surface = pygame.image.load('graphics/bomb.png').convert_alpha()
scorpion_surface3 = pygame.image.load('graphics/scorpion3.png').convert_alpha()
scorpion_surface2 = pygame.image.load('graphics/scorpion2.png').convert_alpha()
scorpion_surface1 = pygame.image.load('graphics/scorpion1.png').convert_alpha()
chest_surface = pygame.image.load('graphics/chest.png').convert_alpha()
hole_surface = pygame.image.load('graphics/hole.png').convert_alpha()
hole_surface1 = pygame.image.load('graphics/hole_fall_6.png').convert_alpha()
hole_surface2 = pygame.image.load('graphics/hole_fall_5.png').convert_alpha()
hole_surface3 = pygame.image.load('graphics/hole_fall_4.png').convert_alpha()
hole_surface4 = pygame.image.load('graphics/hole_fall_3.png').convert_alpha()
hole_surface5 = pygame.image.load('graphics/hole_fall_2.png').convert_alpha()
hole_surface6 = pygame.image.load('graphics/hole_fall_1.png').convert_alpha()
stars_surface1 = pygame.image.load('graphics/stars1.png').convert_alpha()
stars_surface2 = pygame.image.load('graphics/stars2.png').convert_alpha()
stars_surface3 = pygame.image.load('graphics/stars3.png').convert_alpha()
stars_surface4 = pygame.image.load('graphics/stars4.png').convert_alpha()
stars_surface5 = pygame.image.load('graphics/stars5.png').convert_alpha()
stars_surface6 = pygame.image.load('graphics/stars6.png').convert_alpha()
explosion_surface = pygame.image.load('graphics/explosion.png').convert_alpha()
locker_surface = pygame.image.load('graphics/locker.png').convert_alpha()
player_in_hole_surface = pygame.image.load('graphics/player-in-hole.png').convert_alpha()
card_frame_surface= pygame.image.load('graphics/card_frame.png').convert_alpha()
princess_surface = pygame.image.load('graphics/princess.png').convert_alpha()
cardX = 430 - card_frame_surface.get_width()/2
cardY = 330 - card_frame_surface.get_height()/2
card_num_players_surface = pygame.image.load('graphics/card_num_players.png')
card_help_surface = pygame.image.load('graphics/card_help.png')
card_surface0 = pygame.image.load('graphics/card_00.png')
card_surface1 = pygame.image.load('graphics/card_01.png')
in_arrow_surface = pygame.image.load('graphics/in_arrow.png').convert_alpha()
out_arrow_surface = pygame.image.load('graphics/out_arrow.png').convert_alpha()
hand_surface = pygame.image.load('graphics/hand.png').convert_alpha()
castle_surface = pygame.image.load('graphics/castle.png')
heart_surface = pygame.image.load('graphics/heart.png').convert_alpha()

knight_moving_anim = [knight_surface1_blue, knight_surface2_blue, knight_surface3_blue,
                      knight_surface1_red, knight_surface2_red, knight_surface3_red,
                      knight_surface1_green, knight_surface2_green, knight_surface3_green,
                      knight_surface1_yellow, knight_surface2_yellow, knight_surface3_yellow]
hole_isfalling_anim = [hole_surface1, hole_surface2, hole_surface3, hole_surface4, hole_surface5, hole_surface6]
chest_isopening_anim = [stars_surface1, stars_surface2, stars_surface3, stars_surface4, stars_surface5, stars_surface6]
dice_rolling_anim = (dice_surface1, dice_surface2, dice_surface3, dice_surface4, dice_surface5, dice_surface6)
card_list = [card_surface0, card_surface1]

# Sounds:
knight_walkingsound = pygame.mixer.Sound('sounds/cartoon-jump.mp3')
dice_rollingsound = pygame.mixer.Sound('sounds/dice-rolling-sound.mp3')
fanfare_sound = pygame.mixer.Sound('sounds/tada-fanfare.mp3')
bomb_sound = pygame.mixer.Sound('sounds/hq-explosion.mp3')
scorpion_sound = pygame.mixer.Sound('sounds/scorpion_bite.mp3')
hole_sound = pygame.mixer.Sound('sounds/hole-falling.mp3')
sad_sound = pygame.mixer.Sound('sounds/so-sad.mp3')
chest_sound = pygame.mixer.Sound('sounds/opening-chest.mp3')
nono_sound = pygame.mixer.Sound('sounds/nono-sound.mp3')
pop_sound = pygame.mixer.Sound('sounds/pop.mp3')
vanish_sound = pygame.mixer.Sound('sounds/vanish.mp3')
punch_sound = pygame.mixer.Sound('sounds/punch.mp3')

item_image = (scorpion_surface1, scorpion_surface2, scorpion_surface3, bomb_surface,
              chest_surface, hole_surface,in_arrow_surface,out_arrow_surface)
item_image_name = ('escorpião1', 'escorpião2', 'escorpião3', 'bomba', 'baú', 'buraco','setaentrada','setasaida')

# Forma a estrutura de itens no tabuleiro e armazena numa lista
def sets_struct():
    items = []
    items.clear()
    maxitems = 7
    for position in range(64):
        item_random = random.randrange(0, maxitems)
        if item_random == 1 or item_random == 2:
            item_random = 0
        if item_random > len(item_image):
            item_random = 0

        items.append(item_random)
    items[0] = 7
    items[56] = 8
    if debug_mode:
        print(items)
    return items

items = sets_struct()

# Calcula a posição do objeto de acordo com o número do quadrado no tabuleiro
def get_coordinates(my_position, invert):
    my_inverse = int(my_position / 8) % 2
    my_inversion = my_inverse * (7 - 2 * int(my_position % 8))
    my_inverted_pos = my_position + my_inversion
    if invert:
        X = (my_inverted_pos * 100 + diagonal_adjust) % 800
    else:
        X = (my_position * 100 + diagonal_adjust) % 800
    Y = int(my_position / 8) * 75 + diagonal_adjust
    return (X + 4, Y, my_inverse, my_inverted_pos)

# Adianta um jogador
def goto_next_player(current):
    current += 1
    if current > number_of_players -1:
        current = 0
    return current
# Mostra mensagens na tela
def show_message(my_message,myfont_size,x,y,r,g,b):
    my_font = pygame.font.SysFont('Comic Sans MS', myfont_size)
    text_surface = my_font.render(my_message, True, (r, g, b))
    screen.blit(text_surface, (x - text_surface.get_width()/2, y - text_surface.get_height()/2))

def show_card(my_surface):
    screen.blit(my_surface,(cardX+32,cardY+38))
    screen.blit(card_frame_surface,(cardX,cardY))

# Entrada no jogo

fanfare_sound.play()

# LOOP PRINCIPAL
while True:

    # Pausa o jogo
    if keyboard.is_pressed('p') and key_delay == 0:
        key_delay = 15
        game_paused = not game_paused
    key_delay -= 1
    if key_delay < 0:
        key_delay = 0

    if game_paused:
        if int(frame_counter / 10 % 2):
            show_message('GAME PAUSED',96,430,330, 255,0,0)
        else:
            show_message('GAME PAUSED', 96, 430, 330, 0, 0, 0)

    if not game_paused:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Detecção de eventos (teclado etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if card_isshowing > 0:
                    card_isshowing = 0
                # Ajuda
                if event.key == pygame.K_F1:
                    help_mode = not help_mode
                # Modo debug
                if event.key == pygame.K_ESCAPE:
                    debug_mode = not debug_mode
                    pygame.display.set_caption("MAGICAL ADVENTURE")
                if event.key == pygame.K_TAB and debug_mode:
                    player_pos[current_player] = 59
                if not critical_animation and not help_mode:
                    # Joga o dado
                    if ((event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_a)
                            and player_steps == -1):
                        dice_rollingsound.play()
                        dice_isrolling = random.randrange(16, 32)
                        player_direction = 1

        # Desenha o tabuleiro e alguns itens fixos
        screen.blit(background_surface, (0, 0))
        #screen.blit(flag_surface, (40,564))

        # Mostra o dado girando e o valor
        if dice_isrolling > 1 and frame_counter % 2:
            dice_side = random.randrange(1, 6)
            dice_isrolling -= 1
        elif dice_isrolling == 1:
            dice_isrolling = 0
            player_steps = dice_side + 1
        elif dice_isrolling == 0:
            player_initial_pos = player_pos[current_player]
            if player_initial_pos + player_steps > 63:
                player_steps = 63 - player_initial_pos
            if frame_counter % 2:
                steps_way += 1
            if steps_way > player_steps:
                steps_way = 1
            arrowX, arrowY, inverse_arrow, arrow_inverted_pos = get_coordinates(player_initial_pos + steps_way, True)
        screen.blit(dice_rolling_anim[dice_side], (928, 490))

        # desenha os itens na tela
        for position in range(64):
            # adiciona efeito de flutuação a determinados itens
            Y_fluctuation += fluctuation_factor
            if Y_fluctuation > max_fluctuation or Y_fluctuation < 0:
                fluctuation_factor = -fluctuation_factor

            # seleciona o item que está na posição para mostrar na tela

            itemX, itemY, inverse, inverted_pos = get_coordinates(position, False)
            itemX = itemX
            itemY = itemY - (Y_fluctuation * (items[position] < 4 and items[position] > 0)
                             + (max_fluctuation - Y_fluctuation) * (items[position] == 4)
                             + (max_fluctuation - Y_fluctuation / 2) * ((items[position] == 5) or (items[position]==7)
                                                                        or (items[position]==8)))
            if items[position] > 0 and items[position] < len(item_image) + 1:
                screen.blit(item_image[items[position]-1], (itemX, itemY))
            if debug_mode:
                text_surface = my_font.render(str(items[position]), False, (0, 0, 0))
                screen.blit(text_surface, (itemX - 10, itemY - 10))

        # Animação do Jogador (Knight)
        knight_anim += 1
        if knight_anim >= 30:
            knight_anim = 0
        for current_showing in range(current_player-number_of_players+1, current_player+1):
            # if current_showing > -1:
            current_player_showing = (current_showing * (current_showing > -1)) + (abs(number_of_players + current_showing) * (current_showing < 0))
            # elif current_showing < 0:
            #     current_player_showing = abs(number_of_players + current_showing)
            if debug_mode:
                print (current_player_showing)
            playerX, playerY, inverse, player_inverted_pos = get_coordinates(abs(player_pos[current_player_showing]), True)
            if player_pos[current_player_showing] == -1:
                playerX = playerpool_pos[0] + 14 + current_player_showing % 2 * 96
                playerY = playerpool_pos[1] + 4 + int(current_player_showing / 2) * 96
                inverse = 1
            if player_pos[current_player_showing] < -1:
                screen.blit(player_in_hole_surface,
                            (playerX + current_player_showing * 6 *
                             (player_pos[current_player_showing] > -1), playerY))
            knight_image = knight_moving_anim[int(knight_anim / 10) + current_player_showing * 3]
            if inverse > 0:
                knight_image = pygame.transform.flip(
                    knight_moving_anim[int(knight_anim / 10) + current_player_showing * 3], True, False)
            if ((current_player_showing != exploding_player) and (current_player_showing != falling_player)
                    and (player_pos[current_player_showing] > -2)):
                screen.blit(knight_image,
                            (playerX - 10 + current_player_showing * 6 *
                             (player_pos[current_player_showing] > -1), playerY - 16))
            # Mão indicadora
            if current_player_showing == current_player and player_steps < 1 and not critical_animation:
                if int(frame_counter / 10) % 2:
                    screen.blit(hand_surface, (playerX + 8, playerY - 42 + Y_fluctuation))

        # Mostra a seta na tela indicando a direção
        if inverse_arrow > 0:
            arrow_image = pygame.transform.flip(arrow_surface, True, False)
        else:
            arrow_image = arrow_surface
        arrow_Show = (player_pos[current_player] > -1) and (player_steps > 0) and player_direction == 1
        if arrow_Show:
            screen.blit(arrow_image, (arrowX + 8, arrowY + 8))
        playerX, playerY, inverse, player_inverted_pos = get_coordinates(player_pos[current_player], True)

        # Move o Jogador de acordo com o numero do Dado ou Ação do Item
        if player_steps > 0:
            if player_direction == 1:
                player_speed = 30
            else:
                player_speed = 10
            step_counter += 1
            if step_counter == player_speed:
                player_pos[current_player] += player_direction
                if player_pos[current_player] == 63:
                    player_won = current_player
                    pygame.mixer.music.load('sounds/ending_song.mp3')
                    pygame.mixer.music.play()
                if player_won > -1 and not critical_animation:
                    game_isinend = 60*20
                if player_pos[current_player] < 0:
                    player_pos[current_player] = 0
                knight_walkingsound.play()
                player_steps -= 1
                step_counter = 0
        if player_steps == 0:
            playerX, playerY, inverse, player_inverted_pos = get_coordinates(player_pos[current_player], True)
            player_steps = -1

            # Quadrado Vazio
            if items[player_inverted_pos] < 1 or player_pos[current_player] == 0:
                items[player_inverted_pos] = (current_player + 1) * -1
                current_player = goto_next_player(current_player)
                collision = False

        # Detecção de obstáculos
        player_is_stopped = player_steps == -1 and player_pos[current_player] > -1

    # Passa a vez do jogador se ele estiver no buraco
        if player_pos[current_player] < -1 and not critical_animation:
            player_pos[current_player] = player_pos[current_player] * -1
            nono_sound.play()
            player_isexitinghole = 120
        if player_isexitinghole > 0:
            if int(frame_counter / 10) % 2:
                screen.blit(locker_surface, (playerX-16, playerY - 16))
                player_isexitinghole -= 1
        if player_isexitinghole == 0:
            player_isexitinghole = -1
            current_player = goto_next_player(current_player)

        # Outro jogador
        if player_is_stopped:
            if items[player_inverted_pos] < 0:
                collision = True

        # Escorpiões:
        if player_is_stopped and not critical_animation:
            if items[player_inverted_pos] > 0 and items[player_inverted_pos] < 4 and scorpion_isstinging == -1:
                items[player_inverted_pos] = items[player_inverted_pos] - 1
                scorpion_sound.play()
                collision = True
                scorpion_isstinging = 180
                stung_player = current_player
                player_direction = -1
                if player_pos[current_player] > 5:
                    player_steps = 5
                elif player_pos[current_player] < 6:
                    player_steps = player_pos[current_player]
        if scorpion_isstinging > 0:
            scorpion_isstinging -= 1
        if scorpion_isstinging == 0:
            scorpion_isstinging = -1
            stung_player = -1

        # Bombas:
        if player_is_stopped and not critical_animation:
            if items[player_inverted_pos] == 4 and bomb_isexploding == -1:
                items[player_inverted_pos] = 0
                bomb_sound.play()
                collision = True
                bomb_isexploding = 24
                bombX, bombY, inverse, player_inverted_pos = get_coordinates(player_pos[current_player], True)
                exploding_player = current_player
        if bomb_isexploding > 0:
            if frame_counter % 2:
                screen.blit(explosion_surface, (bombX - 92, bombY - 96))
                bomb_isexploding -= 1
        if bomb_isexploding == 0:
            sad_sound.play()
            bomb_isexploding = -1
            player_pos[exploding_player] = -1
            exploding_player = -1
            current_player = goto_next_player(current_player)

        # Baús:
        if player_is_stopped and not critical_animation:
            if items[player_inverted_pos] == 5 and chest_isopening == -1:
                items[player_inverted_pos] = (current_player + 1) * -1
                chest_sound.play()
                collision = True
                chest_isopening = 6
                chestX, chestY, inverse, player_inverted_pos = get_coordinates(player_pos[current_player], True)
                prized_player = current_player
        if chest_isopening > 0:
            screen.blit(chest_isopening_anim[chest_isopening - 1], (chestX - 16, chestY - 16))
            if frame_counter % 8 == 0:
                chest_isopening -= 1
        if chest_isopening == 0:
            chest_isopening = -1
            prized_player = -1
            card_taken = random.randrange(0, 2)
            if debug_mode:
                print (card_taken)
            card_isshowing = 200
            pop_sound.play()

        # Buracos:
        if player_is_stopped and not critical_animation:
            if items[player_inverted_pos] == 6 and hole_isfalling == -1:
                items[player_inverted_pos] = (current_player + 1) * -1
                hole_sound.play()
                collision = True
                hole_isfalling = 6
                holeX, holeY, inverse, player_inverted_pos = get_coordinates(player_pos[current_player], True)
                falling_player = current_player
        if hole_isfalling > 0:
            screen.blit(hole_isfalling_anim[hole_isfalling - 1], (holeX, holeY))
            if frame_counter % 8 == 0:
                hole_isfalling -= 1
        if hole_isfalling == 0:
            hole_isfalling = -1
            player_pos[falling_player] = player_pos[falling_player] * - 1
            falling_player = -1
            current_player = goto_next_player(current_player)

        # Mostra a carta do prêmio
        if card_isshowing > 0:
            show_card(card_list[card_taken])
            card_isshowing -= 1
        if card_isshowing == 0:
            card_isshowing = -1
            vanish_sound.play()

        # Gera a recompensa de acordo com o prêmio
        if card_isshowing == -1:
            if card_taken == 0:
                player_steps = 5
                player_direction = 1
                card_taken = -1
            if card_taken == 1:
                card_taken = -1

        # Mostra o menu de entrada
        if game_isinmenu > 0:
            if game_isinmenu == 2 and number_of_players == 0:
                show_card(card_num_players_surface)
                if keyboard.is_pressed('1'):
                    number_of_players = 1
                if keyboard.is_pressed('2'):
                    number_of_players = 2
                if keyboard.is_pressed('3'):
                    number_of_players = 3
                if keyboard.is_pressed('4'):
                    number_of_players = 4
            if number_of_players > 0:
                punch_sound.play()
                game_isinmenu = 0
        # Mostra a ajuda
        if help_mode:
            show_card(card_help_surface)


        # Mostra animação do final do jogo
        if player_won > -1:
            screen.blit(castle_surface, (8, 8))
            screen.blit(princess_surface, (690, 420))
            screen.blit(knight_image, (752, 430))
            if int(frame_counter / 10) % 2:
                screen.blit(heart_surface, (732, 370))
            game_isinend -= 1

        if game_isinend == 0:
            player_won = -1
            number_of_players = 0
            player_pos = [-1, -1, -1, -1]
            player_initial_pos = [-1, -1, -1, -1]
            current_player = 0
            player_steps = -1
            player_direction = 1
            collision = False
            steps_way = 0
            step_counter = 0
            arrowX = 0
            arrowY = 0
            inverse_arrow = 0
            knight_anim = 0
            dice_isrolling = -1
            bomb_isexploding = -1
            scorpion_isstinging = -1
            hole_isfalling = -1
            chest_isopening = -1
            player_isexitinghole = -1
            card_isshowing = -1
            card_taken = -1
            exploding_player = -1
            stung_player = -1
            falling_player = -1
            prized_player = -1
            dice_side = 0
            game_isinmenu = 2
            game_isinend = -1
            items = sets_struct()

        # Mostra dados de telemetria no prompt para verificação
        if debug_mode:
            pygame.display.set_caption(f'MODO DEBUG (<ESC> para sair) - frame: {frame_counter}//pos. jogador: {player_pos}'
                                       f'//coord. jogador: {playerX, playerY}'
                                       f'//jogador atual: {current_player} //fim de jogo {game_isinend}'
                                       f'// mouse: X-{mouse_x} Y-{mouse_y}')

        critical_animation = (((bomb_isexploding > -1) or (scorpion_isstinging > -1 or (hole_isfalling > -1))
                              or (chest_isopening > -1) or (player_isexitinghole > -1) or (card_isshowing > -1))
                              or (game_isinmenu > 0) or (game_isinend > -1))

    # Desenha todos os elementos
    # Atualiza tudo
    pygame.display.update()
    frame_counter += 1
    if frame_counter > fps_rate-1:
        frame_counter = 0
    clock.tick(fps_rate)

# FIM DO LOOP PRINCIPAL
