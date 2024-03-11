import tkinter
from datetime import timedelta
from tkinter import*
 
 
class Cronom(Frame):
 
    def __init__(self, master=None):
        Frame.__init__(self, master)
        tkinter.Frame.__init__(self, master)
        self.master = master
 
        self.fontePadrao = ("Arial", "20")
 
 
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 15
        self.primeiroContainer.pack()
 
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack(side=tkinter.LEFT)
 
        self.area = Label(self.primeiroContainer,width=10, font=self.fontePadrao,text='0:00:00')
        self.area.pack()
 
        self.area.config(state="normal",justify=tkinter.CENTER)
 
        self.iniciar = Button(self.segundoContainer)
        self.iniciar["text"] = "Iniciar"
        self.iniciar["font"] = ("Calibri", "8")
        self.iniciar["width"] = 12
        self.iniciar["command"] = self.Contar
        self.iniciar.pack(side=tkinter.LEFT)
 
        self.pausa = Button(self.segundoContainer)
        self.pausa["text"] = "Pausar"
        self.pausa["font"] = ("Calibri", "8")
        self.pausa["width"] = 12
        self.pausa["command"] = self.Pausar
        self.pausa.pack(side=tkinter.LEFT)
 
        self.zera = Button(self.segundoContainer)
        self.zera["text"] = "Zerar"
        self.zera["font"] = ("Calibri", "8")
        self.zera["width"] = 12
        self.zera["command"] = self.Zerar
        self.zera.pack(side=tkinter.LEFT)
 
    def Contar(self):
 
        global tempo
        global ativado
        global clique
 
        clique = 0
        ativado = True
        tempo = timedelta(seconds=0)
        self.iniciarContagem()
 
    def iniciarContagem(self):
 
        global ativado
        global tempo
        global clique
 
        self.Contagem()
 
    def Contagem(self):
 
        global tempo
        global ativado
        global clique
 
        if tempo != timedelta and ativado == True :
            root.after(930, self.iniciarContagem)
            self.iniciar.config(state="disabled")
            self.pausa.config(state="normal")
            tempo = tempo + timedelta(seconds=1)
            self.area['text'] = tempo
 
    def Pausar(self):
 
        global tempo
        global ativado
        global clique
 
 
        try:
 
            self.iniciar.config(state="disabled")
            self.pausa.config(state="normal")
            self.pausa["text"] = "Continuar"
            ativado = False
            tempo = tempo
            self.verificaClique(1)
 
        except NameError:
            pass
 
    def verificaClique(self,cliques):
 
        global tempo
        global ativado
        global clique
 
        clique = clique+cliques
 
        if clique == 2:
            ativado = True
            self.pausa["text"] = "Pausar"
            self.Contagem()
            clique = 0
 
    def Zerar(self):
 
        global tempo
 
        self.iniciar.config(state="normal")
        tempo = timedelta(seconds=0)
        self.area['text']=('0:00:00')
 
 
root = tkinter.Tk()
root.geometry("250x150+1000+500")
root.title("Dobrio cronometro")
root.resizable(height=FALSE,width=FALSE)
Cronom(root)
root.mainloop()