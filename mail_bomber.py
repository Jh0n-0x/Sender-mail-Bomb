#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from Tkinter import *
	
		# Titutlo: Sender mail
		# plataforma: pyhton
		# Criado por: Pablo Santhus
		# Link Software: https://github.com/PabloSanthus/senderMail-python
		# help: sendermail.py


def enviar_msg():
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()

	email = txtb.get()
	senha = txtb1.get()

	server.login(email, senha)

	mensagem = txtb2.get()
	para = txtb3.get()
	bomber = txtb4.get()

	num = 1
	while(num <= bomber):
		send = server.sendmail(email, para, mensagem)
		num+1

	if(send):
		lb4["text"]='Nao Enviado'
	else:
		lb4["text"]='Enviado com sucesso para ' + email

def sair():
	janela.destroy()

janela=Tk()

lbl = Label(janela, text="Sender Email", fg="blue")
lbl.place(x=120, y=5)
lbl['font']=('arial', '15', 'bold')

lbl1 = Label(janela, text="Criado by: Pablo Santhus")
lbl1.place(x=250, y=15)
lbl1['font']=('arial', '8', 'bold')

# ----------------------------------------

lb = Label(janela, text="Email:", fg="blue")
lb.place(x=20, y=30)
lb['font']=('arial', '12', 'bold')

txtb = Entry(janela)
txtb.place(x=115, y=34)
txtb['width'] = 50

# ----------------------------------------

lb1 = Label(janela, text="Senha:", fg="blue")
lb1.place(x=20, y=60)
lb1['font']=('arial', '12', 'bold')

txtb1 = Entry(janela)
txtb1.place(x=115, y=68)
txtb1['width'] = 50

# ----------------------------------------

lb2 = Label(janela, text="Mensagem:", fg="blue")
lb2.place(x=20, y=90)
lb2['font']=('arial', '12', 'bold')

txtb2 = Entry(janela)
txtb2.place(x=115, y=95)
txtb2['width'] = 50


# ----------------------------------------


lb3 = Label(janela, text="Para:", fg="blue")
lb3.place(x=20, y=118)
lb3['font']=('arial', '12', 'bold')

txtb3 = Entry(janela)
txtb3.place(x=115, y=122)
txtb3['width'] = 50

# ----------------------------------------

lb4 = Label(janela, text="Bomber:", fg="blue")
lb4.place(x=20, y=150)
lb4['font']=('arial', '12', 'bold')

txtb4 = Entry(janela)
txtb4.place(x=115, y=156)
txtb4['width'] = 50


# ----------------------------------------

btn = Button(janela, text="Enviar", command=enviar_msg)
btn.place(x=20, y=180)
btn['width']=20
btn['height']=2
btn['bg']='green'
# ----------------------------------------

btn = Button(janela, text="Sair", command=sair)
btn.place(x=300, y=180)
btn['width']=20
btn['height']=2
btn['bg']='red'
# ----------------------------------------

lb5 = Label(janela, text="status", fg="red")
lb5.place(x=20, y=223)

# ----------------------------------------


janela.title("Sender Email")
janela.geometry("480x244")
janela.mainloop()
