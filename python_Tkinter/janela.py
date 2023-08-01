from tkinter import *
import tkinter

#cores 
cor1 = '#7f5c67'

janela = Tk()
janela.title('Ola Mundo')
janela.geometry('600x250')
janela.config(bg=cor1)

janela.iconphoto(FALSE, PhotoImage(file='logoandroid.png'))
janela.resizable(width=False,height=True)

janela.mainloop()