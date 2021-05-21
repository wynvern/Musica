from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from time import sleep

mixer.init()

se01 = True
co02 = True

try:
    st03 = open('configs.txt', 'r')
    in04 = float(st03.read())
    st03.close()
except FileNotFoundError:
    st03 = open('configs.txt', 'w')
    st03.write('0.2')
    st03.close()

    st03 = open('configs.txt', 'r')
    in04 = float(st03.read())
    st03.close()

mixer.music.set_volume(in04)

# Principal, serve para colocar a musica
while se01 is True:
    co02 = True
    mu05 = str(input('Escreva o nome da música para reproduzir: ')).strip().lower()
    mp06 = '.mp3' in mu05 

    if mu05 == 'sair': 
        se01, co02 = False
    else:
        if mp06 is False: 
            mu05 = mu05 + '.mp3'
    
    mixer.music.load(mu05)
    sleep(0.5)
    mixer.music.play()
    print('')

    # Segundo, comandos e outros
    while co02 is True:
        co07 = str(input('Comando para a música: ')).strip().lower()
        
        if mixer.music.get_busy() == 0:
            se01 = False

        if co07 is 'sobre':
            print('')
            print('\033[1;35mFoi o Zeki quem fez! Versão 0.1.3')
            print('Alguns bugs estão a solta pelo programa, eu vou corrigir eles...')
            print('Espero que você goste do que eu fiz >w<\033[m')
            print('')

        vo08 = + float(in04)
        vo09 = 'volume' in co07
        if vo09 is True:
            print('')
            vo08 = co07.split()
            if vo09[1] is 'info':
                print('O volume da musica e {:.0f}'.format(mixer.music.get_volume() * 100))
                print('')
            else:
                vo10 = float(vo08[1]) / 100
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
            musica2 = ''
            comandos = + 1

        if co07 == 'sair':
            sair = + 1
            comandos = + 1

        if co07 == 'recomecar':
            mixer.music.rewind()

        
print('')
print('\033[1;31mSaindo do programa... Tchau!\033[m')
print('')
mixer.music.fadeout(200)
sleep(1)
