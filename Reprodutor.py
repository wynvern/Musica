from os import environ
from time import sleep
import threading
import keyboard
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer, error
del environ

mixer.init()

global voltar_musica
global var
co02, te19, li16, voltar_musica, var, tocando_musicas_diretorio, tocando_musicas_lista, thread_iniciado = True, False, [], 0, False, False, False, False

def ativador_cores(cor, momento):
    if momento == 0:
        if mostrar_cores == 1: print(cor) 
        else: print('')
    else: print(cor)
        
def comandos_teclado(tecla, comando):
    try:
        if keyboard.is_pressed(tecla):
                comando()
                sleep(2)
        else:
            sleep(0.1)
    except:
        sleep(0.1)


def Teclado_atalhos():
    while True:    
        if var is True: break
        if tocando_musicas_diretorio or tocando_musicas_lista is True:
            comandos_teclado('ctrl+', proxima)
            comandos_teclado('ctrl+[', voltar)


def voltar():
    global voltar_musica
    voltar_musica = 1
    mixer.music.unload()

def proxima():
    global te19
    mixer.music.unload()
    te19 = False


def editor_arquivo():
    mixer.music.set_volume(vo10)
    arquivo_configs = open('configs.txt', 'w')
    arquivo_configs.writelines(str(vo10))
    arquivo_configs.writelines('\n')
    arquivo_configs.writelines(str(mostrar_cores))
    arquivo_configs.close()


def arquivo_errado(mensagem):
    print(mensagem)
    print('')
    arquivo_configs = open('configs.txt', 'w')
    arquivo_configs.write('0.2\n')
    arquivo_configs.write('0')
    arquivo_configs.close()


def is13():
    global thread_iniciado
    global tocando_musicas_diretorio
    global tocando_musicas_lista
    global li16
    global in18
    global var
    global voltar_musica
    global li16
    global contador
    global numero_atual_tocando
    thread_iniciado = True
    numero_atual_tocando = 0
    contador = 0
    while True:
        if var is True:
            var = False
            thread_iniciado = False
            break

        if te19 is False:
            if tocando_musicas_lista is True:
                if voltar_musica == 1:
                    numero_atual_tocando = numero_atual_tocando - 2
                    voltar_musica = 0
                if mixer.music.get_busy() == 0:
                    if numero_atual_tocando >= in18 and numero_atual_tocando << 0:
                        numero_atual_tocando = numero_atual_tocando - numero_atual_tocando
                    
                    if numero_atual_tocando != in18:
                        try:
                            try:
                                mixer.music.load(li16[numero_atual_tocando])

                            except IndexError:
                                thread_iniciado = False
                                break
                            mixer.music.play()
                            numero_atual_tocando = numero_atual_tocando + 1
                        except error:
                            li16.remove(li16[numero_atual_tocando])
                            in18 = in18 - 1
                            numero_atual_tocando = numero_atual_tocando + 1
                            continue
            
            if tocando_musicas_diretorio is True:
                if voltar_musica == 1:
                    numero_atual_tocando = numero_atual_tocando - 2
                    voltar_musica = 0
                if mixer.music.get_busy() == 0:
                    try:
                        musica_tocar = arquivos_velho + procura_arquivos[numero_atual_tocando]

                    except IndexError:
                        thread_iniciado = False
                        break
                    contador = 0
                    mixer.music.load(musica_tocar)
                    mixer.music.play()
                    numero_atual_tocando = numero_atual_tocando + 1
        
        contador = contador + 1
        sleep(0.9)


try:
    st03 = open('configs.txt', 'r')
    in04 = float(st03.readline())
    mostrar_cores = (int(st03.readline()))
    st03.close()
except FileNotFoundError:
    arquivo_errado('Erro, arquivo desaparecido')
    st03 = open('configs.txt', 'r')
    in04 = float(st03.readline())
    mostrar_cores = int(st03.readline())
    st03.close()
except ValueError:
    arquivo_errado('Erro, arquivo modificado incorretamente')
    st03 = open('configs.txt', 'r')
    in04 = float(st03.readline())
    mostrar_cores = int(st03.readline())
    st03.close()

mixer.music.set_volume(in04)
vo10 = in04

print('Bem vindo ao reprodutor')
print('')

threading.Thread(target=Teclado_atalhos).start()

#Tudo começa depois daqui!
while co02 is True:
    co07 = str(input('Comando para a música: ')).strip().lower()

    certeza = 'tocar' in co07
    if certeza is True:
        sera_tocado = co07.replace('tocar', '').strip()
        if mixer.get_busy() == 1:
            certeza = 's'
            certeza = str(input('Para tocar {} voce precisa parar o que esta sendo tocado (S/N)'.format(sera_tocado))).lower().strip()
        
        else:    
            if certeza == 's' or 'sim':
                tocando_musicas_lista = False
                tocando_musicas_diretorio = False
                mixer.music.unload()
                mixer.music.unpause()
                li15 = 0
                li16 = []
                tem_mp3 = '.mp3' in sera_tocado
                if tem_mp3 is False:
                    sera_tocado = sera_tocado + '.mp3'
                li16.append(sera_tocado)

    if co07 == 'proxima':
        proxima()
    
    if co07 == 'tempo':
        try:
            print('A musica esta a {}'.format(contador))
        except NameError:
            continue
        print('')

    if co07 == 'pasta':
        tocando_musicas_diretorio = False
        tocando_musicas_lista = False
        import glob
        mixer.music.fadeout(200)
        localizacao_arquivos = str(input('Cole a localização dos seus arquivos de música: ')).strip() + '\*.mp3'
        procura_arquivos = glob.glob(localizacao_arquivos)
        arquivos_velho = localizacao_arquivos.replace('*.mp3', '').strip()
        for numero_atual in range(0, 99):
            try:
                procura_arquivos[numero_atual] = procura_arquivos[numero_atual].replace(arquivos_velho, '').strip()

            except IndexError:
                continue

        tocando_musicas_lista = False
        tocando_musicas_diretorio = True
        del glob
        if thread_iniciado is True:
            var = True
            sleep(0.1)
            var = False
            threading.Thread(target=is13).start()
        else: threading.Thread(target=is13).start()

    if co07 == 'lista':
        contador = 0
        quantidade_de_musicas = 0
        tocando_musicas_diretorio = False
        tocando_musicas_lista = False
        mixer.music.fadeout(200)
        in18 = -1
        li16 = []
        en26 = False
        li15 = 0
        for musicas in range(0, 99):
            if en26 is False:
                li16.append(str(input('Nome da música: ')))
                if li16[li15] == '#':
                    en26 = True
                else:
                    contador = contador + 1
                    mp06 = '.mp3' in li16[li15]
                    if mp06 is False:
                        li16[li15] = li16[li15] + '.mp3'

                li15 = li15 + 1
                in18 = in18 + 1
                quantidade_de_musicas = quantidade_de_musicas + 1
            else: li16.append(str('#'))
               
            if li16[musicas] == '#': en26 = True
               
        if en26 is True:
            for remocao in range(99 - contador): li16.remove('#')
                    
        print('')
        tocando_musicas_lista = True
        if thread_iniciado is True:
            var = True
            sleep(0.1)
            var = False
            threading.Thread(target=is13).start()
        else: threading.Thread(target=is13).start()

    qe12 = 'queue' in co07
    if qe12 is True:
        print('')
        co07 = co07.replace('queue', '').strip()
        mp06 = 'mp3' in co07
        if mp06 is False:
            co07 = co07 + '.mp3'

        valor_musicas_nao_tocadas = None
        valor_musicas_nao_tocadas = in18
        valor_musicas_ja_tocadas = 0
        lista_ja_tocado = []
        tirar_antigo = 0
        lista_temporaria = []
        lista_temporaria = li16
        

        for tirar_antigo in range(0, numero_atual_tocando): lista_ja_tocado.append(lista_temporaria[tirar_antigo])

        for tirar_antigo_outro in range(numero_atual_tocando):
            lista_temporaria.remove(lista_temporaria[0])
            valor_musicas_ja_tocadas = valor_musicas_ja_tocadas + 1

        li16 = []

        for recriador_lista in range(0, valor_musicas_ja_tocadas): li16.append(lista_ja_tocado[recriador_lista])
        
        valor_musicas_nao_tocadas = valor_musicas_nao_tocadas - valor_musicas_ja_tocadas

        li16.append(co07)
        in18 = in18 + 1

        for recriado_lista_outro in range(0, valor_musicas_nao_tocadas):
            li16.append(lista_temporaria[recriado_lista_outro])

        
    if co07 == 'voltar': voltar()

    if co07 == 'sobre':
        ativador_cores('\033[1;35m', 0)
        print('Foi o Zeki quem fez! Versão 0.1.6')
        print('Alguns bugs estão a solta pelo programa, eu vou corrigir eles...')
        print('Espero que você goste do que eu fiz >w<')
        ativador_cores('\033[m', 1)

    vo08 = + float(in04)
    vo09 = 'volume' in co07
    if vo09 is True:
        vo08 = co07.split()
        if vo08[1] == 'info':
            print('')
            print('O volume da música é {:.0f}'.format(mixer.music.get_volume() * 100))
            print('')
        else:
            try:
                vo10 = float(vo08[1]) / 100
            except ValueError:
                print('O valor digitado é inválido')
                print('')
                continue

        editor_arquivo()

    if co07 == 'pausar':
        mixer.music.pause()
        te19 = True

    if co07 == 'musica':
        if tocando_musicas_diretorio is True: print('O nome da musica sendo reproduzida e {}'.format(procura_arquivos[numero_atual]))
        else: print('O nome da musica sendo reproduzida e {}'.format(li16[li15]))
            
    if co07 == 'retomar':
        mixer.music.unpause()
        te19 = False

    if co07 == 'cores':
        if mostrar_cores == 0: mostrar_cores = 1
        else: mostrar_cores = 0
        st03 = open('configs.txt', 'w')
        editor_arquivo()

    if co07 == 'sair': co02, var = False, True

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


mixer.music.fadeout(200)
var = True

from os import system, name
ativador_cores('\033[1;31m', 0)

for vezes in range(0, 4):
    sleep(0.5)
    system('cls' if name == 'nt' else 'clear')
    print('Saindo do programa' + '.' * vezes)

ativador_cores('\033[m', 1)
sleep(0.5)
