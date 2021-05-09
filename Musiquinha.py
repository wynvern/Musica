from pygame import mixer
from time import sleep
mixer.init()

sair = 0
comandos = 0

configs = open('configs.txt', 'r')
info = float(configs.read())
configs.close()

if info == 0.0:
    ok = 1
else:
    configs = open('configs.txt', 'w')
    configs.write('5')
    configs.close()




mixer.music.set_volume(info)

while sair == 0:   
    comandos = 0
    
    musica = str(input('Escreva o nome da musica para reproduzir: ')).strip()
    
    if musica == 'sair':
        sair =+ 1
        comandos =+ 1
    else:
        mp3 = '.mp3' in musica
        if mp3 == False:
            musica = musica + '.mp3'

        mixer.music.load(musica)
        sleep(0.5)
        mixer.music.play()
    
    print('')
    
    while comandos == 0:
        comando = str(input('Comando para a musica: ')).strip()
        comando = comando.lower()
        
        tocando = mixer.music.get_busy()
        if tocando == 0:
            comandos = 1
        
        if comando == 'info':
            print('')
            print('\033[1;35mFoi o Zeki quem fez! Versao 0.1.2')
            print('Alguns bugs estao a solta pelo programa, eu vou corrigir eles...')
            print('Espero que voce goste do que eu fiz >w<\033[m')
            print('')

        if comando == 'volume':
            print('')
            volume = float(input('Volume: '))
            
            mixer.music.set_volume(volume)
            configs = open('configs.txt', 'w')
            configs.write(str(volume))
            configs.close()
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

        if comando == 'alistar':
            musica2 = str(input('Escreva o nome da musica para alistar: ')).strip()
            mp31 = '.mp3' in musica2
            if mp31 == False:
                musica2 = musica2 + '.mp3'

            mixer.music.queue(musica2)
            
            print('')                    
            print('\033[1;32mA musica {} foi alistada com sucesso e tocara depois de {}\033[m'.format(musica2, musica))
            print('')
                                
            if mixer.music.queue(musica2):
                musica2 = 0
                     

print('\033[1;31mSaindo do programa... Tchau!\033[m')
mixer.music.fadeout(200)
sleep(1)
