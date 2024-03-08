#03/10/2023
#@PLima
#ROBO - BACKUP PASTA C:
import pyautogui
import datetime
import time
import sys
import os
import tkinter as tk
import threading

import signal

#para sair da automacao colocando o mouse no topo a esquerda da janela
pyautogui.FAILSAFE = True
status = True
statusThread = False

def pausa(tempo):
    print("time de:" , tempo)
    time.sleep(tempo)   
    
def fechando_explorer():
    pausa(5)
    print("Fechando explorer;")
    pyautogui.hotkey("win" , "d")#("Alt" , "f4")
    pausa(2)   

def agora():
    agora = datetime.datetime.now()
    agora = agora.strftime("%d/%m/%Y %H:%M:%S")
    return str(agora)
    
def fim():
    global status
    #fechando_explorer()    
    print("Backup finalizado com sucesso!")      
    pyautogui.alert("     Backup finalizado com sucesso!     " , timeout=1000000)
    status = False
    print(f"Status: {status}")
    print("==================================== FIM ====================================")    
    #sys.exit()
    #fechando_explorer()
    
def log(texto_):
    if not os.path.exists("log.txt"):
            with open("log.txt" , "a" , encoding="utf-8-sig") as log:
                print(f'Log é {os.path.exists("log.txt")}, então será criado na pasta')
                log.write("")
                        
    with open("log.txt" , "a", encoding="utf-8-sig")  as log:
        log.write(f"\n{str(texto_)} - {str(agora())}")   
            

def botao_Apps():
    #botao para habilitar as opções
    print("botao para habilitar as opções;")
    pyautogui.hotkey("apps")
    pausa(1)
    #posicao do 7 zip
    pyautogui.hotkey("7")
    #4x down:
    print("4x teclado down;")
    pyautogui.hotkey("down")
    pyautogui.hotkey("down")
    pyautogui.hotkey("down")
    pyautogui.hotkey("down")
    pausa(1)
    print("Enter botao_Apps;")
    pyautogui.hotkey("enter")
    pausa(60)
    
def backup_Projetos():
    print("***Função Backup Projetos***")
    log("Função Backup Projetos - início")
    print("Tecla windows + R;")
    pyautogui.hotkey("win" , "r")
    pausa(1)
    print("Inserindo: C:\Pietro")
    pyautogui.write("C:\Pietro")
    pausa(1)
    print("Enter;")
    pyautogui.hotkey("enter")
    pausa(1)
    print("click na pasta;")
    pyautogui.click(975 , 531)
    pausa(1)
    pyautogui.hotkey("win" , "up")
    pausa(1)
    print("Projetos")
    pyautogui.write("Projetos")
    botao_Apps()
    #selecionando arquivo zip recem criado
    print("selecionando arquivo zip recem criado")
    pausa(60)
    pyautogui.write("Projetos.zip")
    pausa(1)
    pyautogui.hotkey("f2")
    pausa(1)
    print("Registrando momento atual;")
    agora = datetime.datetime.now()    
    print("Agora: " , str(agora))    
    renomear = "Projetos_" + agora.strftime("%d/%m/%Y-%H:%M:%S")
    print("Renomear: " , renomear)
    pyautogui.write(renomear)
    pausa(2)
    print("enter")
    pyautogui.hotkey("enter")
    pausa(1)
    print("ctrl + x;")
    pyautogui.hotkey("ctrl" , "x")
    pausa(2)
    fechando_explorer()
    print("Tecla windows + R;")
    pyautogui.hotkey("win" , "r")
    pausa(1)
    print("Inserindo: C:\Pietro\OneDrive - PRONEP\Backup")
    pyautogui.write("C:\Pietro\OneDrive - PRONEP\Backup")
    pausa(1)
    print("Enter;")
    pyautogui.hotkey("enter")
    pausa(2)
    print("click na pasta;")
    #pyautogui.click(526,522)
    pyautogui.hotkey("win" , "up")    
    pausa(2)
    print("ctrl + v;")
    pyautogui.hotkey("ctrl" , "v")
    pausa(5)
    #todo
    fechando_explorer()
    log("Função Backup Projetos - fim")    
     

def backup_MV_QUERYs():
    print("Função Backup MV QUERYS - início")
    log("Função Backup MV QUERYS - início")
    print("Tecla windows + R;")
    pyautogui.hotkey("win" , "r")
    pausa(1)
    print("backspace")
    pyautogui.hotkey("backspace")
    pausa(1)
    print("Inserindo: C:\Pietro\OneDrive - PRONEP")
    pyautogui.write("C:\Pietro\OneDrive - PRONEP")
    pausa(1)
    print("enter")
    pyautogui.hotkey("enter")
    pausa(1)
    print("click na pasta;")
    pyautogui.click(975 , 531)
    pausa(1)
    pyautogui.hotkey("win" , "up")
    pausa(1)
    print("16. Homologação")
    pyautogui.write("16. Homologação ")
    pausa(2)
    print("enter")
    pyautogui.hotkey("enter")
    pausa(1)
    print("MV QUERY")
    pyautogui.write("MV QUERY")
    pausa(1)
    botao_Apps()
    pausa(1)
    #selecionando arquivo zip recem criado
    print("selecionando arquivo zip recem criado")
    pausa(30)
    pyautogui.write("MV QUERYs.zip")
    pausa(2)
    print("f2")
    pyautogui.hotkey("f2")
    pausa(2)
    print("Registrando momento atual;")
    agora = datetime.datetime.now()    
    print("Agora: " , str(agora))    
    renomear = "MV_QUERYs_" + agora.strftime("%d/%m/%Y-%H:%M:%S")
    print("Renomear: " , renomear)
    pyautogui.write(renomear)
    pausa(2)
    print("enter")
    pyautogui.hotkey("enter")
    pausa(2)
    print("ctrl + x;")
    pyautogui.hotkey("ctrl" , "x")
    pausa(2)
    fechando_explorer()
    print("Tecla windows + R;")
    pyautogui.hotkey("win" , "r")
    pausa(1)
    print("Inserindo: C:\Pietro\OneDrive - PRONEP\Backup")
    pyautogui.write("C:\Pietro\OneDrive - PRONEP\Backup")
    pausa(1)
    print("Enter;")
    pyautogui.hotkey("enter")
    pausa(2)
    print("click na pasta;")
    #pyautogui.click(526,522)
    pyautogui.hotkey("win" , "up")    
    pausa(2)
    print("ctrl + v;")
    pyautogui.hotkey("ctrl" , "v")
    pausa(5)
    #todo
    #fechando_explorer()
    log("Função Backup MV QUERYS - fim")    
    
def backup_IW_QUERIES_HOME_CARE():
    print("Função Backup IW QUERIES HOME CARE - início")
    log("Função Backup IW QUERIES HOME CARE - início")        
    pausa(2)
    print("win + r")
    pyautogui.hotkey("win" , "r")
    pausa(1)
    print("backspace;")
    pyautogui.hotkey("backspace")
    pausa(1)
    print("C:\Pietro\OneDrive - PRONEP")
    pyautogui.write("C:\Pietro\OneDrive - PRONEP")
    pausa(1)
    print("enter;")
    pyautogui.hotkey("enter")
    pausa(1)
    print("16. Homologação;")
    pyautogui.write("16. Homologação ")
    pausa(2)
    print("enter;")    
    pyautogui.hotkey("enter")
    pausa(1)
    print("IW QUERIES HOME_CARE;")
    pyautogui.write("IW QUERIES HOME_CARE")
    pausa(1)
    botao_Apps()
    pausa(1)
    #selecionando arquivo zip recem criado
    pausa(5)
    print("selecionando arquivo zip recem criado;")
    pyautogui.write("IW QUERIES HOME_CARE.zip")
    pausa(1)
    print("f2;")
    pyautogui.hotkey("f2")
    pausa(1)
    print("Registrando momento atual;")
    agora = datetime.datetime.now()    
    print("Agora: " , str(agora))    
    renomear = "IW_QUERIES_HOME_CARE_" + agora.strftime("%d/%m/%Y-%H:%M:%S")
    print("Renomear: " , renomear)
    pyautogui.write(renomear)
    pausa(2)
    print("enter;")
    pyautogui.hotkey("enter")
    pausa(1)
    print("ctrl + c;")
    pyautogui.hotkey("ctrl" , "x")
    pausa(2)
    #todo
    #fechando_explorer()
    pausa(1)    
    print("Tecla windows + R;")
    pyautogui.hotkey("win" , "r")
    pausa(1)
    print("Inserindo: C:\Pietro\OneDrive - PRONEP\Backup")
    pyautogui.write("C:\Pietro\OneDrive - PRONEP\Backup")
    pausa(1)
    print("Enter;")
    pyautogui.hotkey("enter")
    pausa(2)
    print("click na pasta;")
    pyautogui.hotkey("win" , "up")    
    pausa(2)
    print("ctrl + v;")
    pyautogui.hotkey("ctrl" , "v")
    pausa(5)
    #todo
    fechando_explorer()
    log("Função Backup IW QUERIES HOME CARE - fim")        


#funcao abaixo concentra todas as tarefas em fila e executa:
def Executar():
    print(f"#==================================== Executar()")
    global status
    try:
        while status:
            time.sleep(1)
            if status==False:
                print(f"dentro do if;\nstatus: {status}")
                print("Execucao paralizada!")
                break
            print(f"Status no while: {status}")
            print("Iniciando...")
            backup_Projetos()
            backup_MV_QUERYs()
            backup_IW_QUERIES_HOME_CARE()
            fim()
    except Exception as erro:
        print(f"log.close() {agora()}\nErro: {erro=}, {type(erro)=}")  

def pausar():
    global statusThread
    statusThread=False
    print(f"global statusThread: {statusThread}")
    print("============================== Pausar() ========================")



#==================================== INÍCIO ====================================
def interface():
    root = tk.Tk()
    root.maxsize(720,500)
    root.minsize(360,250)
    root.geometry("360x250")
    root.title("ROBO - BACKUP PASTA C")
    root.configure(bg="white")
    
    
    def start():        
        global statusThread
        #criando evento na thread, para ser usado apos ser setado, ser verificado e encerrar a thread
        if statusThread:
            print(f"Thread já foi iniciada, statusThread: \n{statusThread}")
        else:        
            #iniciando thread para usar na funcao Executar()    
            threadExecutar = threading.Thread(target=Executar).start()
            #threadExecutar.start()
            statusThread = True
            print(f"statusThread: {statusThread}\nthreadExecutar.start()\n")
    
    imagem = tk.PhotoImage(file="BACKUP.png")
    lb_barra_superior = tk.Label(root, image=imagem , border =0)
    lb_barra_superior.pack()
    
    bt_Iniciar = tk.Button(root, text="Iniciar", command=lambda: [ print("Botao Iniciar") , lb_console.config(text="Robo inicializado!") , start()])
    bt_Iniciar.pack(fill="both", expand=True , padx=100 , pady=5 )    

    bt_Sair = tk.Button(root, text="Fechar", command=lambda: [ print("Botao Fechar") , lb_console.config(text="Robo pausado!") , os.kill(os.getpid(), signal.SIGINT)])
    bt_Sair.pack(fill="both", expand=True , padx=100 , pady=5)
    
    lb_console = tk.Label(root, text="...não inicializado...")
    lb_console.pack(fill="both" , expand=True , pady=10)    
    
    root.mainloop()  
try:
    if __name__ == "__main__":
        print("==================================== INÍCIO ====================================")
        interface()

except KeyboardInterrupt:
    print("==================================== FIM ====================================")
    print("Interrompido pelo ctrl + c!!!\n")        
except Exception as erro:
    print("==================================== FIM ====================================")
    print(f"Erro: {erro=}, {type(erro)=}")  