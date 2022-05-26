import tkinter
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageFont, ImageDraw

def water():
    #Opening Image
    im = fd.askopenfilename()
    img = Image.open(im)

    #Creating draw object
    draw = ImageDraw.Draw(img)
    text = input_water.get()
    font = ImageFont.truetype('arial.ttf', 60)
    textwidth, textheight = draw.textsize(text, font)
    width, height = img.size
    x=width/2-textwidth/2   #center
    y=height-textheight-300
    draw.text((x, y), text, font=font)

    img.save(r'watermarked.png')
    win = Toplevel()
    succ = Label(win, text="success")
    succ.grid(column=0, row=0)

window = Tk()
window.title("Watermark")
window.minsize(width=500, height=300)    #window size
inst = Label(text="Write your watermark")
inst.grid(column=0, row=0)
input_water = Entry(width=20)
input_water.grid(column=1, row=0)
watermark_button = Button(text="Watermark", command=water)
watermark_button.grid(column=2, row=0)

window.mainloop()
