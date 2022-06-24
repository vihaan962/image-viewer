# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:52:33 2022

@author: VIHAAN KATHURIA
"""

from tkinter import*
root = Tk()
root.title("Image Viewer")
root.geometry("600x600")
root.config(bg = "black")

btn = Button(root,text = "Open Image", bg = "grey", fg = "white")
btn.place(relx = 0.5, rely = 0.2, anchor = CENTER)

label_image = Label(root,bg = "white")
label_image.place(relx = 0.5, rely = 0.5, anchor = CENTER )

btn1 = Button(root,text = "Rotate Image", bg = "grey", fg = "white")
btn1.place(relx = 0.5, rely = 0.8, anchor = CENTER)

root.mainloop()