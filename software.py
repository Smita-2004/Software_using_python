import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser,filedialog , messagebox
import os

main_application =tk.Tk()
main_application.geometry('800x500')
main_application.title("Vpad text editor")


###################################### main menu ###################################
# ------------------------------$$$$$$$$ End main menu &&&&&&&&-----------------------
main_menu =tk.Menu()

#file
file = tk.Menu(main_menu,tearoff=False)



edit= tk.Menu(main_menu,tearoff=False)
view = tk.Menu(main_menu,tearoff=False)
color_theme = tk.Menu(main_menu,tearoff=False)

#cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color_theme)

###################################### toolbar ###################################
# ------------------------------$$$$$$$$ End toolbar &&&&&&&&-----------------------


###################################### text editor ###################################
# ------------------------------$$$$$$$$ End text editor &&&&&&&&-----------------------


###################################### main status bar ###################################
# ------------------------------$$$$$$$$ End main status bar &&&&&&&&-----------------------



###################################### main menu functionality ###################################
# ------------------------------$$$$$$$$ End main menu functionality &&&&&&&&-----------------------
main_application.config(menu=main_menu)
main_application.mainloop()