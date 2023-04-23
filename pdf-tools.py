#!/usr/bin/env python3

# todo:
#  - log window, welcome message
#  - docstrings
#  - PEP8
#  - create safeguards and checks
#  - pythonic project and script structure


import os
from datetime import datetime
from pypdf import PdfReader
from pypdf import PdfWriter
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox


def split_pdfs():
    """Splits PDFs in working directory."""
    # Create PDF writer objects to add pages to
    pdf_writer_front = PdfWriter()
    pdf_writer_back = PdfWriter()

    # Loop through files for PDFs with even pages
    count = 0  # Count for total files split
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            # Create PDF reader to handle files
            pdf_reader = PdfReader(filename)

            if len(pdf_reader.pages) % 2 == 0:
                count = count + 1
                pdf_writer_front.append(fileobj=pdf_reader, pages=(0, (int(len(pdf_reader.pages) / 2))))
                pdf_writer_back.append(fileobj=pdf_reader,
                                       pages=(int(len(pdf_reader.pages) / 2), int(len(pdf_reader.pages))))

    current_time = str(datetime.now())

    frontOutput = open(current_time + "FRONTOUTPUT.pdf", "wb")
    backOutput = open(current_time + "BACKOUTPUT.pdf", "wb")
    pdf_writer_front.write(frontOutput)
    pdf_writer_back.write(backOutput)

    pdf_writer_front.close()
    pdf_writer_back.close()
    messagebox.showinfo("PDF Split Completed", f"{count} file(s) split.")


def merge_pdfs():
    """Merges PDFs in working direction."""
    pass  # add PDF merge script later


def pdf_tools_gui():
    """Starts tkinter GUI loop for running pdf-tools scripts."""
    root = Tk()
    frame = ttk.Frame(root, padding=10)  # Frame widget to fit in root window
    frame.grid()
    ttk.Label(frame, text="pdf-tools scripts").grid(column=0, row=0)
    ttk.Button(frame, text="Split PDFs", command=split_pdfs).grid(column=0, row=1)
    ttk.Button(frame, text="Merge PDFs", command=merge_pdfs).grid(column=0, row=2)
    ttk.Button(frame, text="Exit", command=root.destroy).grid(column=0, row=3)
    root.mainloop()


def main():
    """Main function, executed if module is run as a script."""
    pdf_tools_gui()  # Start tkinter GUI


# If module is run as a script, execute main()
if __name__ == '__main__':
    main()
