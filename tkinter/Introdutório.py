from tkinter import Label  #get a widget
widget = Label(None, text='hello world') #make a Label
widget.pack() #arrange it in its parent
widget.mainloop() #start the event loop