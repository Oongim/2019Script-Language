import tkinter
from CustomTkClass import *

vpWindow = Viewport(0, 0, 1200, 800)

window = tkinter.Tk()
window.geometry \
            ("{width}x{height}+{left}+{top}".format(width=vpWindow.width, height=vpWindow.height,
                                                    left=vpWindow.left, top=vpWindow.top))


# def __init__(self, window, viewport, widthRatioKindLabel, padRatiosAtCenter, kindText, detaText):
label = DescLabel(window, vpWindow, 0.3, 0.2, "KIND", "DEST")
label.place(vpWindow.left, vpWindow.top, "nw")
# TempFont = tkinter.font.Font(window, size=20, weight='bold', family='Consolas')
#
# label = tkinter.Label(window,  font=TempFont, text="text", width=10, height=1, bg = "Red", anchor="e")
# label.place(x=vpWindow.width//2, y=vpWindow.height//2)
window.mainloop()