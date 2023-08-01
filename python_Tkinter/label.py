from tkinter import *

janela = Tk()
janela.title('Label')
janela.geometry('250x250')

label_nome = Label(janela, width=10, height=2, text='Nome: ', font=('Arial 15'), fg='#4d7b99', bg='black')
label_nome.grid(row=0, column=0, pady=10)

label_idade = Label(janela, width=10, height=2, text='Idade: ', font=('Arial 15 bold'), fg='#4d9958', bg='black')
label_idade.grid(row=1, column=0, pady=10)

label_email = Label(janela, width=10, height=2, text='Email: ', font=('Arial 15'), fg='#99974d', bg='black')
label_email.grid(row=2, column=0, pady=10)



janela.mainloop()