import pygame
pygame.mixer.init()

sair = 0
comandos = 0

while sair == 0:
    
    comandos = 0
    
    musica = str(input('Escreva o nome da musica para reproduzir: '))
    musica.strip()
    
    print('')
    musica = musica + '.mp3'
    
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()

    while comandos == 0:
        comando = str(input('Comando para a musica: '))
        print('')

        if comando == 'pausar':
            pygame.mixer.music.pause()
        else:
            if comando == 'retomar':
                pygame.mixer.music.unpause()
            else:
                if comando == 'trocar':
                    pygame.mixer.music.unload()
                    comandos =+ 1
                else:
                    if comando == 'sair':
                        sair =+ 1
                        comandos =+ 1
                    else:
                        if comando == 'recomecar':
                            pygame.mixer.music.rewind()
                        else:
                            if comando == 'alistar':
                                musica2 = str(input('Escreva o nome da musica para alistar: '))
                                musica2.strip()
                                musica2 = musica2 + '.mp3'

                                pygame.mixer.music.queue(musica2)
                                
                                print('A musica {} foi alistada com sucesso e tocara depois de {}'.format(musica2, musica))
                                print('')
                                
                                if pygame.mixer.music.queue(musica2):
                                    musica2 = 0
            
