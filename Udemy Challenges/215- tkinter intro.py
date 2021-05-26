try:
    import tkinter
except ImportError:   # if youre running python 2
    import Tkinter as tkinter


print(tkinter.TkVersion)
print(tkinter.TclVersion)

##################
# to run a sample gui
#
#tkinter._test()
#
##################

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480')
mainWindow.mainloop()