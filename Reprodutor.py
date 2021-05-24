from os import environ
import glob
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import threading
from pygame import mixer
from time import sleep

mixer.init()

se01, co02, te11, te19 = True, True, False, False
tocando_musicas_diretorio = False
li16 = []

global var
var = False

def thread():
    threading.Thread(target=is13).start()

def is13():
    ne21 = 0
    li15 = 0
    for tocando in range(999):
        if var == True:
            break
        else:
            if te19 is False:
                if tocando_musicas_diretorio is False:
                    if mixer.music.get_busy() == 0:
                        if li15 != in18:
                            try: 
                                mixer.music.load(li16[li15])
                                mixer.music.play()
                                li15 = li15 + 1
                            except pygame.error:
                                li15 = li15 + 1
                                continue
                        else:      
                            ne21 = 0
                    else:
                        ne21 = 0
                else:
                    if mixer.music.get_busy() == 0:
                        musica_tocar = arquivos_velho + procura_arquivos[li15]
                        mixer.music.load(musica_tocar)
                        mixer.music.play()
                        li15 = li15 + 1
                    else:
                        ne21 = 0
        sleep(1)

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
    var = False
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

        if co07 == 'proxima':
            mixer.music.unload()
            te19 = False

        if co07 == 'pasta':
            localizacao_arquivos = str(input('Digite a localizacao dos seus arquivos de musica: ')).strip() + '\*.mp3'
            procura_arquivos = glob.glob(localizacao_arquivos)
            arquivos_velho = localizacao_arquivos.replace('*.mp3', '').strip()
            for numero_atual in range(0, 99):
                try:
                    procura_arquivos[numero_atual] = procura_arquivos[numero_atual].replace(arquivos_velho, '').strip()
    
                except IndexError:
                    continue
            
            tocando_musicas_diretorio = True
            thread()

        if co07 == 'alistar':
            tocando_musicas_diretorio = False
            in18 = -1
            en26 = False
            li15 = 0
            for musicas in range(0,99):
                if en26 == False:
                    li16.append(str(input('Nome da musica: ')))
                    if li16[li15] == '#':
                        en26 is True
                    else:
                        mp06 = '.mp3' in li16[li15]
                        if mp06 is False:
                            li16[li15] = li16[li15] + '.mp3'

                    li15 = li15 + 1
                    in18 = in18 + 1
                else:
                    li16.append(str('#'))
    
                if li16[musicas] == '#':
                    en26 = True

            if en26 is True:
                for remocao in range(0,99):
                    try:
                        li16.remove('#')
                    except ValueError:
                        continue

            thread()
            
        qe12 = 'queue' in co07
        if qe12 is True:
            co07 = co07.replace('queue', '').strip()
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
            te19 = True

        if co07 == 'retomar':
            mixer.music.unpause()
            te19 = False

        if co07 == 'trocar':
            mixer.music.unload()
            co02, se01, var, li15 = False, True, True, 0
            li16.clear()

        if co07 == 'sair':
            co02, se01, var = False, False, True

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
