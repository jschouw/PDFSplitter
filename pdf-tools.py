#!/usr/bin/env python3


import os
from datetime import datetime
from pypdf import PdfReader
from pypdf import PdfWriter
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox


def pdf_tools_gui():
    """Starts tkinter GUI loop for running pdf-tools scripts."""
    root = Tk()
    frame = ttk.Frame(root, padding=20)  # Frame widget to fit in root window
    frame.grid()
    ttk.Label(frame, text="pdf-tools\n").grid(column=0, row=0)
    ttk.Button(frame, text="Split PDFs", command=split_pdfs).grid(column=0, row=1)
    ttk.Button(frame, text="Merge PDFs", command=merge_pdfs).grid(column=0, row=2)
    ttk.Button(frame, text="Exit", command=root.destroy).grid(column=0, row=3)
    root.mainloop()


def split_pdfs():
    """Splits PDFs in working directory.

    Splits all PDF files in half by page number and outputs two long PDF files
    of the merged halves.
    """
    pdf_writer_front = PdfWriter()
    pdf_writer_back = PdfWriter()

    # Loop through files for PDFs with even pages
    count = 0  # Count for total files split
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            # Create PDF reader to handle files
            pdf_reader = PdfReader(filename)
            # Only split files if they have an even number of pages
            if len(pdf_reader.pages) % 2 == 0:
                count = count + 1  # Increase count by 1
                pagecount = len(pdf_reader.pages)
                pdf_writer_front.append(fileobj=pdf_reader, pages=(0, int(pagecount / 2)))
                pdf_writer_back.append(fileobj=pdf_reader, pages=(int(pagecount / 2), pagecount))

    if count == 0:
        return messagebox.showerror(title="Error: No files", message="Error: No PDF files to split.")

    current_time = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    front_output = open(current_time + "-front-split-output.pdf", "wb")
    back_output = open(current_time + "-back-split-output.pdf", "wb")
    pdf_writer_front.write(front_output)
    pdf_writer_back.write(back_output)
    pdf_writer_front.close()
    pdf_writer_back.close()
    messagebox.showinfo("PDF Split Completed", f"{count} file(s) split.")


def merge_pdfs():
    """Merges PDFs in working directory."""

    pdf_writer = PdfWriter()
    count = 0  # Count for total files merged
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            pdf_reader = PdfReader(filename)
            count = count + 1
            pdf_writer.append(fileobj=pdf_reader)

    if count <= 1:
        return messagebox.showerror(title="Error: Not enough files",
                                    message="Error: Not enough PDF files to complete merge operation.")

    current_time = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    output = open(current_time + "-merged_output.pdf", "wb")
    pdf_writer.write(output)
    pdf_writer.close()
    messagebox.showinfo("PDF Merge Completed", f"{count} files merged.")


def main():
    """Main function, executed if module is run as a script."""
    pdf_tools_gui()  # Start tkinter GUI


# If module is run as a script, execute main()
if __name__ == '__main__':
    main()
