from tkinter import *

janela = Tk()
janela.title('Label')
janela.geometry('250x250')

label_nome = Label(janela, width=10, height=2, text='Nome: ', font=('Arial 15'), fg='#4d7b99', bg='black')
label_nome.pack()

nome = Label(janela, width=10, height=2, text='LUIZ ', font=('Arial 15'), fg='#4d7b99', bg='black')
nome.pack()

label_idade = Label(janela, width=10, height=2, text='Idade: ', font=('Arial 15 bold'), fg='#4d9958', bg='black')
label_nome = Label(janela, width=10, height=2, text='38', font=('Arial 15'), fg='#4d7b99', bg='black')


label_email = Label(janela, width=10, height=2, text='Email: ', font=('Arial 15'), fg='#99974d', bg='black')
label_nome = Label(janela, width=10, height=2, text='lulavalenca ', font=('Arial 15'), fg='#4d7b99', bg='black')



janela.mainloop()