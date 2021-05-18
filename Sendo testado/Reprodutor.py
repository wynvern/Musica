from pygame import mixer
from time import sleep

import pygame
mixer.init()

sair = 0
comandos = 0

try:
    configs = open('configs.txt', 'r')
    info = float(configs.read())
    configs.close()
except FileNotFoundError:
    configs = open('configs.txt', 'w')
    configs.write('0.5')
    configs.close

    configs = open('configs.txt', 'r')
    info = float(configs.read())
    configs.close()

mixer.music.set_volume(info)

while sair == 0:   
    comandos = 0
    
    musica = str(input('Escreva o nome da música para reproduzir: ')).strip().lower()

    if musica == 'sair':
        sair =+ 1
        comandos =+ 1
    else:
        mp3 = '.mp3' in musica
        if mp3 == False:
            musica = musica + '.mp3'

        try:
            mixer.music.load(musica)
            sleep(0.5)
            mixer.music.play()
        except pygame.error:
            print('A musica {} nao existe'.format(musica))


    print('')
    
    while comandos == 0:
        comando = str(input('Comando para a música: ')).strip().lower()
        
        tocando = mixer.music.get_busy()
        if tocando == 0:
            proxima = arquivo.readline()
            mixer.music.queue(proxima)
        
        if comando == 'sobre':
            print('')
            print('\033[1;35mFoi o Zeki quem fez! Versão 0.1.3')
            print('Alguns bugs estão a solta pelo programa, eu vou corrigir eles...')
            print('Espero que você goste do que eu fiz >w<\033[m')
            print('')
        
        v1 =+ float(info)
        v0 = 'volume' in comando
        if v0 == True:
            print('')
            v1 = comando.split()
            if v1[1] == 'info':
                print('O volume da musica e {:.0f}'.format(mixer.music.get_volume() * 100))
                print('')
            else:
                try:
                    volume = float(v1[1]) / 100
                    mixer.music.set_volume(volume)
                    configs = open('configs.txt', 'w')
                    configs.write(str(volume))
                    configs.close()
                except ValueError:
                    print('Valor digitado invalido')
                    print('')

        if comando == 'pausar':
            mixer.music.pause()
        
        if comando == 'retomar':
            mixer.music.unpause()

        if comando == 'trocar':
            mixer.music.unload()
            musica2 = ''
            comandos =+ 1

        if comando == 'sair':
            sair =+ 1
            comandos =+ 1            

        if comando == 'recomecar':
            mixer.music.rewind()                

        if comando == 'automatico':
            musiquinhas = []
            playlist = int(input('Quantidade de musicas: '))

            arquivo = open('teste.txt', 'w')
            for linha in range(0, playlist):
                
                musiquinhas.append(str(input('nome da musica: ')))
                mp3teste = '.mp3' in musiquinhas[linha]
                if mp3teste == False:
                    arquivo.write(musiquinhas[linha] + '.mp3')
                else:
                    arquivo.write(musiquinhas[linha])
                arquivo.write('\n')
    
            arquivo = open('teste.txt', 'r')
            musicas = arquivo.readline().strip()

            mixer.music.queue(musicas)
            
            print('')                    
            print('\033[1;32mA música {} foi alistada com sucesso e tocará depois de {}\033[m'.format(musicas, musica))
            print('')
                                
                     
print('')
print('\033[1;31mSaindo do programa... Tchau!\033[m')
print('')
mixer.music.fadeout(200)
sleep(1)