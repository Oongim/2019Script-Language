from GmailAndXMLSaveLoadFrame import GmailAndXMLSaveLoadFrame
import tkinter
from CustomTkClass import Viewport

viewport = Viewport(0,0, 800, 600)
window = tkinter.Tk()
window.geometry \
    ("{width}x{height}+{left}+{top}".format(width=viewport.width, height=viewport.height,
                                            left=viewport.left, top=viewport.top))
GmailAndXMLSaveLoadFrame(1, window, viewport)

window.mainloop()