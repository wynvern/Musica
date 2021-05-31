from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer, error
del environ
from time import sleep
import glob
import threading

mixer.init()

global voltar_musica
global var
se01, co02, te11, te19, li16, pular_inicio, voltar_musica, var = True, True, False, False, [], False, 0, False

def thread():
    threading.Thread(target=is13).start()


def is13():
    global voltar_musica
    numero_atual_tocando = 0
    neutro = 0
    while True:
        if var:
            break

        if te19 is False:
            if tocando_musicas_diretorio is False:
                if voltar_musica == 1:
                    numero_atual_tocando = numero_atual_tocando - 2
                    voltar_musica = 0
                if mixer.music.get_busy() == 0:
                    if numero_atual_tocando != in18:
                        try:
                            try:
                                mixer.music.load(li16[numero_atual_tocando])

                            except IndexError:
                                break
                            mixer.music.play()
                            numero_atual_tocando = numero_atual_tocando + 1
                        except error:
                            numero_atual_tocando = numero_atual_tocando + 1
                            continue
            else:
                if voltar_musica == 1:
                    numero_atual_tocando = numero_atual_tocando - 2
                    voltar_musica = 0
                if mixer.music.get_busy() == 0:
                    try:
                        musica_tocar = arquivos_velho + procura_arquivos[numero_atual_tocando]
                    
                    except IndexError:
                        print('')
                        print('Não existem arquivos de música nesse diretório')
                        print('')
                        break
                    mixer.music.load(musica_tocar)
                    mixer.music.play()
                    numero_atual_tocando = numero_atual_tocando + 1
                else:
                    neutro = 0
        sleep(0.5)


try:
    st03 = open('configs.txt', 'r')
    in04 = float(st03.readline())
    mostrar_cores = (int(st03.readline()))
    st03.close()
except FileNotFoundError:
    st03 = open('configs.txt', 'w')
    st03.write('0.2\n')
    st03.write('0')
    st03 = open('configs.txt', 'r')
    in04 = float(st03.readline())
    mostrar_cores = int(st03.readline())
    st03.close()

mixer.music.set_volume(in04)

while se01 is True:
    var = False
    co02 = True
    if te11 is True:
        print('')

    mu05 = str(input('Nome da música para reproduzir: ')).strip().lower()

    if mu05 == 'sair':
        se01, co02 = False, False
    else:
        if mu05 == '':
            pular_inicio = True
            from os import system, name
            system('cls' if name == 'nt' else 'clear')
            del system, name
        else:
            mp06 = '.mp3' in mu05
            if mp06 is False:
                mu05 = mu05 + '.mp3'

        if pular_inicio is False:
            try:
                mixer.music.load(mu05)
            except error:
                print('')
                print('A música {} não existe, tente outro arquivo'.format(mu05))
                te11 = True
                continue

            sleep(0.5)
            mixer.music.play()

    while co02 is True:
        co07 = str(input('Comando para a música: ')).strip().lower()
        te11 = True

        print('')

        if co07 == 'proxima':
            mixer.music.unload()
            te19 = False
        
        if co07 == 'pasta':
            tocando_musicas_diretorio = True
            localizacao_arquivos = str(input('Cole a localização dos seus arquivos de música: ')).strip() + '\*.mp3'
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
            in18 = 0
            li16 = []
            en26 = False
            li15 = 0
            for musicas in range(0, 99):
                if en26 is False:
                    li16.append(str(input('Nome da música: ')))
                    if li16[li15] == '#':
                        en26 = True
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
                for remocao in range(0, 99):
                    try:
                        li16.remove('#')
                    except ValueError:
                        continue

            print('')
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
            except error:
                print('Música {} não existe'.format(co07))
                print('')
                continue
            print('')

        if co07 == 'voltar':
            voltar_musica = 1
            mixer.music.unload()

        if co07 == 'sobre':
            if mostrar_cores == 1:
                print('\033[1;35m')
            print('Foi o Zeki quem fez! Versão 0.1.6')
            print('Alguns bugs estão a solta pelo programa, eu vou corrigir eles...')
            print('Espero que você goste do que eu fiz >w<')
            if mostrar_cores == 1:
                print('\033[m')
                print('')
            else:
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
                st03 = open('configs.txt', 'w')
                st03.writelines(str(vo10))
                st03.writelines('\n')
                st03.writelines(str(mostrar_cores))
                st03.close()

        if co07 == 'pausar':
            mixer.music.pause()
            te19 = True

        if co07 == 'retomar':
            mixer.music.unpause()
            te19 = False

        if co07 == 'cores':
            if mostrar_cores == 0:
                mostrar_cores = 1
            else:
                mostrar_cores = 0
            
            st03 = open('configs.txt', 'w')
            try:
                st03.writelines(str(vo10))
                st03.writelines('\n')

            except NameError:
                st03.writelines(str(in04))
                st03.writelines('\n')
            st03.writelines(str(mostrar_cores))
            st03.close()


        if co07 == 'trocar':
            mixer.music.unload()
            co02, se01, var, li15, pular_inicio = False, True, True, 0, False
            li16.clear()

        if co07 == 'sair':
            co02, se01, var = False, False, True

        if co07 == 'recomecar':
            mixer.music.rewind()

        if co07 == 'comandos':
            print('''Pausar = Pausa a música
Sair = Sai do programa, também pode ser usado no lugar de perguntar o nome da musica
Retomar = Despausa a música
Proxima = Vai para a próxima música
Voltar = Volta para a antiga música
Trocar = Troca a musica
Queue x= Música em queue, colocar o nome da musica
Alistar = Alistar até 99 músicas, digite # para parar de pedir músicas
Pasta = Toca todas as músicas em formato mp3 de uma pasta sugerida
Recomeçar = Volta a música atual para o início
Volume x = Muda o volume do programa, valores entre 0 e 100
Volume info = Mostra o volume do programa
Comandos = Mostra os possíveis comandos dentro do programa
''')

def sair_diminuir(texto):
    if mostrar_cores == 1:
        print('\033[1;31m')
    sleep(0.5)
    system('cls' if name == 'nt' else 'clear')
    print(texto)

mixer.music.fadeout(200)
from os import system, name

sair_diminuir('Saindo do programa')
for teste in range(1, 4):
    sair_diminuir('Saindo do programa' + '.' * teste)

if mostrar_cores == 1:
    print('\033[m')
else: print('')

sleep(1)
