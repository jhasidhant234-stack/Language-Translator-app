import asyncio
from googletrans import Translator
from tkinter import *
from tkinter import messagebox

# Since default option are allowed , wec check for explicitily given source and destionation language

def translate_function():
    src_v = src_entry.get("1.0","end-1c").strip().lower()
    dest_v = dest_entry.get("1.0","end-1c").strip().lower()
    text_v = text_entry.get("1.0","end-1c").strip()

    if not text_v:
        messagebox.showerror(message="Enter a valid text ")
        return

    async def do_translate():
        async with Translator() as translator:
            if not src_v and not dest_v:
                result = await translator.translate(text_v)
            elif not src_v:
                result = await translator.translate(text_v,dest = dest_v)
            elif not dest_v:
                result = await translator.translate(text_v,src = src_v)
            else:
                result = await translator.translate(text_v,src = src_v,dest= dest_v)
            return result

    try:
        translated_text = asyncio.run(do_translate())
        messagebox.showinfo(message="Translated text : "+ translated_text.text)

    except Exception as e:
        messagebox.showerror(title="Translated Error", message = str(e))




def clear():
    dest_entry.delete("1.0","end-1c")
    src_entry.delete("1.0","end-1c")
    text_entry.delete("1.0","end-1c")


# Invoke call to class to view a window
window = Tk()

# Set dimension of window and title
window.geometry("500x300")
window.title("Language Translator")

# Import the translator class which will read the input and translate_function
# Default translation is done by detection of input and to english
#Title of the app
title_label = Label(window, text="Language Translator Using Python",font=("Gayathri", 12)).pack()
#Read inputs
#Text input
text_label = Label(window, text="Text to translate:").place(x=10,y=20)
text_entry = Text(window, width=40, height=5,font=("Ubuntu Mono",12))
text_entry.place(x=130,y=20)
#Source language input
src_label = Label(window, text="Source language (empty: auto-detect):").place(x=10,y=120)
src_entry = Text(window, width=20,height=1,font=("Ubuntu Mono",12))
src_entry.place(x=275,y=120)
#Destination input
dest_label = Label(window, text="Target language (empty: english-default):").place(x=10,y=150)
dest_entry = Text(window, width=20,height=1,font=("Ubuntu Mono",12))
dest_entry.place(x=300,y=150)
#Translate function and clear function activated through buttons
button1 = Button(window,text='Translate', bg = 'Turquoise',command=translate_function).place(x=160,y=190)
button2 = Button(window,text='Clear', bg = 'Turquoise',command=clear).place(x=270,y=190)
#close the app
window.mainloop()
