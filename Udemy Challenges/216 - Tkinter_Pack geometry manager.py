try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hellow world")
mainWindow.geometry('640x480+8+400')

#writes label at the top of the gui window
label = tkinter.Label(mainWindow, text="Hello")
label.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False )

#creates rectangular canvas within the gui window
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')
#canvas.pack(side='left', fill=tkinter.Y) #expands canvas vertically across the screen
#canvas.pack(side='left', fill=tkinter.X, expand=True) #expands canvas horizontally across the screen
#canvas.pack(side='top', fill=tkinter.Y)
#canvas.pack(side='top', fill=tkinter.X)

#create right frame for buttons
rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)


button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.pack(side='top') #places buttons in north of the window
button2.pack(side='top')
button3.pack(side='top')
#pack is for more simple layout placement

mainWindow.mainloop()
