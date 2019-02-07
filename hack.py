import cx_Oracle
from tkinter import * 
from tkinter import messagebox
from tkinter import scrolledtext
import bs4
import requests
import threading
import time
from PIL import Image,ImageTk
import numpy as np
import matplotlib.pyplot as plt
import socket
import json
from PIL import ImageGrab
from tkinter import filedialog

root=Tk()
#root=Toplevel(root1)
root.title("Add image")
root.geometry("400x400+200+200")
root.resizable(False, False)
def f14():
	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
	#global img2
	#img2=root.filename
	print (root.filename)
	img1 = Image.open(root.filename)
	



btnAdd=Button(root,text="Upload", bg="cyan", fg="black", width=700, height=2, command=f14)

btnAdd.pack()

img = Image.open("tshirt.jpg")
tkimage = ImageTk.PhotoImage(img)
l1=Label(root, image=tkimage)
l1.pack()

image_copy=img.copy()
position=((image_copy.width-img1.width),(image_copy.height-img1.height))
image_copy.paste(img1,position)
image_copy.save('pasted_image.jpg')
	img2 = Image.open("pasted_image.jpg")
	tkimage1 = ImageTk.PhotoImage(img2)
	l2=Label(root, image=tkimage1)
	l2.pack()
		

root.mainloop()