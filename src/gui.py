from tkinter import *
from tkinter.ttk import *
from src.utils import *


def pdf_tools_gui():
    """Starts tkinter GUI loop for running pdf-tools scripts."""

    root = Tk()
    root.title("pdftools")
    frame = Frame(root, padding=5)  # Frame widget to fit in root window
    frame.grid()
    logo = PhotoImage(file="img/logo.png")
    Label(frame, image=logo).grid(column=0, row=0)
    Button(frame, text="Merge PDFs", command=merge_pdfs).grid(column=0, row=1)
    Button(frame, text="Extract text", command=extract_text).grid(column=0, row=3)
    Button(frame, text="Extract images", command=extract_images).grid(column=0, row=4)
    Button(frame, text="Extract metadata", command=extract_metadata).grid(column=0, row=5)
    Button(frame, text="Exit", command=root.destroy).grid(column=0, row=6)
    root.mainloop()
