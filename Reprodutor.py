from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame import mixer
from time import sleep

mixer.init()

se01, co02, te11 = True, True, False

try:
    st03 = open('configs.txt', 'r')
    in04 = float(st03.read())
    st03.close()
except FileNotFoundError:
    st03 = open('configs.txt', 'w')
    st03.write('0.2')
    st03 = open('configs.txt', 'r')
    in04 = float(st03.read())
    st03.close()

mixer.music.set_volume(in04)

# Primeiro, serve para colocar a musica ->
while se01 is True:
    co02 = True
    if te11 is True:
        print('')

    mu05 = str(input('Escreva o nome da música para reproduzir: ')).strip().lower()

    if mu05 == 'sair':
        se01, co02 = False, False
    else:
        mp06 = '.mp3' in mu05
        if mp06 is False:
            mu05 = mu05 + '.mp3'

        try:
            mixer.music.load(mu05)
        except pygame.error:
            print('')
            print('A música {} não existe, tente outro arquivo'.format(mu05))
            te11 = True
            continue

        sleep(0.5)
        mixer.music.play()
        print('')

    # Segundo, comandos e outros ->
    while co02 is True:
        co07 = str(input('Comando para a música: ')).strip().lower()
        te11 = True

        print('')
        
        if mixer.music.get_busy() == 0:
            se01 = False

        qe12 = 'alistar' in co07
        if qe12 is True:
            co07 = co07.replace('alistar', '').strip()
            mp06 = 'mp3' in co07
            if mp06 is False:
                co07 = co07 + '.mp3'

            try:    
                mixer.music.queue(co07)
                print('Música {} alistada com sucesso'.format(co07))
            except pygame.error:
                print('Musica nao existe')
                continue

        if co07 == 'sobre':
            print('')
            print('\033[1;35mFoi o Zeki quem fez! Versão 0.1.5')
            print('Alguns bugs estão a solta pelo programa, eu vou corrigir eles...')
            print('Espero que você goste do que eu fiz >w<\033[m')
            print('')

        vo08 = + float(in04)
        vo09 = 'volume' in co07
        if vo09 is True:
            print('')
            vo08 = co07.split()
            if vo08[1] == 'info':
                print('O volume da música é {:.0f}'.format(mixer.music.get_volume() * 100))
                print('')
            else:
                try:
                    vo10 = float(vo08[1]) / 100
                except ValueError:
                    print('O valor digitado é inválido')
                    print('')
                    continue

                mixer.music.set_volume(vo10)
                configs = open('configs.txt', 'w')
                configs.write(str(vo10))
                configs.close()

        if co07 == 'pausar':
            mixer.music.pause()

        if co07 == 'retomar':
            mixer.music.unpause()

        if co07 == 'trocar':
            mixer.music.unload()
            co02, se01 = False, True

        if co07 == 'sair':
            co02, se01 = False, False

        if co07 == 'recomecar':
            mixer.music.rewind()

        if co07 == 'comandos':
            print('''
Pausar = Pausa a música
Sair = sai do programa, tambem pode ser usado no lugar de perguntar o nome da musica
Retomar = Despausa a música
Trocar = Troca a musica
Alistar x= Música em queue, colocar o nome da musica
Recomeçar = Volta a música atual para o inicio
Volume x = Muda o volume do programa, valores entre 0 e 100
Volume info = Mostra o volume do programa
Comandos = Mostra os possiveis comandos dentro do programa
''')


print('')
print('\033[1;31mSaindo do programa... Tchau!\033[m')
print('')
mixer.music.fadeout(200)
sleep(1)
