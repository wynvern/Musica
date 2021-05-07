from pygame import mixer
mixer.init()

sair = 0
comandos = 0

while sair == 0:   
    comandos = 0
    
    musica = str(input('Escreva o nome da musica para reproduzir: ')).strip()

    mp3 = '.mp3' in musica
    if mp3 == False:
        musica = musica + '.mp3'
    
    print('')
    
    mixer.music.load(musica)
    mixer.music.play()


    while comandos == 0:
        comando = str(input('Comando para a musica: ')).strip()
        comando = comando.lower()
        
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
                                
            print('A musica {} foi alistada com sucesso e tocara depois de {}'.format(musica2, musica))
            print('')
                                
            if mixer.music.queue(musica2):
                musica2 = 0
                     
            