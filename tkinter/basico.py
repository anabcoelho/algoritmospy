from tkinter import *
#Criar nova janela
window= Tk()
# Título da Janela
window.title ('meu programa')
#Entrada de texto
entry_text= Entry (window, width=30)
entry_text.pack ()
entry_text.focus_set

def click_button():
  print (entry_text.get())


btn=Button (window, text= 'clique aqui', width=20, command=click_button)

btn.pack() #gerenciador de geometria

window.geometry ('300x150')

window.mainloop()