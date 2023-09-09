import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk

def add_image():
    global file_path
    file_path = filedialog.askopenfilename(initialdir = "D:\FOLDER" )
    # asks to open file, also gives default directory
    # path of the selected image got saved in file_path
    image = Image.open(file_path)
    #width, height = int(image.width/2), int(image.height/2)
    #image = image.resize((width,height), Image.LANCZOS)
    image = image.resize((900, 600), Image.LANCZOS)

    canvas.config(width= image.width, height= image.height)
    #reshapes the canvas to fit the size of the image.
    image = ImageTk.PhotoImage(image)
    # convert image to an image suitable for tkinter
    canvas.image = image
    canvas.create_image(0,0, image=image, anchor= "nw")
    #image created at 0,0 (origin of the canvas)

def draw(event) :
    x1,y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1,y1,x2,y2, fill = pen_color, outline = '')

    #click event theke - ar + pensize korle circle er duto diamtere end pawa jache
def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title = "Select Pen Color")[1]
def change_size(size) :
    global pen_size
    pen_size= size
def clear_canvas() :
    canvas.delete("all")

def apply_filter(filter) :
    image = Image.open(file_path)
    image = image.resize((900, 600), Image.LANCZOS)
    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur" :
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth" :
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Emboss" :
        image = image.filter(ImageFilter.EMBOSS)

    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")

win = tk.Tk()
win.geometry("1000x600")
win.title(" Image Drawing Tool ")
win.config(bg = "white")

pen_color = "black"
pen_size = 5
file_path = ""

left_frame = tk.Frame(win, width=200, height=600, bg="red")
left_frame.pack(side = "left", fill = "y")
# pack , place and grid - 3 subtypes of placing a container.
# left frame container won't be visible until pack is used

image_button = tk.Button(left_frame, text=" Add Image ", command= add_image)
image_button.pack(pady= 15, padx= 10) # added x and y padding

canvas = tk.Canvas(win,width="750", height="600")
canvas.pack()

canvas.bind("<B1-Motion>" , draw )  #binds the mouse button 1 with a draw function

color_button = tk.Button(
    left_frame, text="Change Pen Color", command=change_color,bg="white" )
color_button.pack(pady=10)

pen_size_frame = tk.Frame(left_frame, bg="white")
pen_size_frame.pack(pady=10)

pen_size_1 = tk.Radiobutton(pen_size_frame, text="small",value=3, command=lambda : change_size(3),bg="white" )
pen_size_1.pack(side="left") #When an argment is to be passed in the function in command, lambda is required
pen_size_2 = tk.Radiobutton(pen_size_frame, text="medium",value=5,command=lambda : change_size(5), bg="white" )
pen_size_2.pack(side="left")
pen_size_2.select() #keeps this selected by default
pen_size_3 = tk.Radiobutton(pen_size_frame, text="large",value=7,command=lambda : change_size(7), bg="white" )
pen_size_3.pack(side="left")

clear_button = tk.Button(left_frame, text="Clear Screen",
                         command=clear_canvas, bg="#FF9797")
clear_button.pack(pady=10)

filter_label = tk.Label(left_frame,text="Filters", bg = "white")
filter_label.pack(pady=10)

filter_combobox = ttk.Combobox(left_frame, values=["Black and White", "Blur",
                                                   "Emboss","Sharpen","Smooth"])
#ttk means themed tkinter. combobox and some thins are available in the ttk sub module

filter_combobox.pack()
filter_combobox.bind("<<ComboboxSelected>>",
                     lambda event: apply_filter(filter_combobox.get()))
win.mainloop()              #keeps the window open


