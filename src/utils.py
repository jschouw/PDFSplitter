#!/usr/bin/env python3

"""
    Functionality and logic of the program, including both GUI creation and PDF manipulation.
"""


# [brainstorming:]
# functionality brainstorming: merge, splice, split, metadata operations, extract text, extract images,
# encrypt/password, reduce file size
# Edit text and images, reorder, and delete pages in a PDF
# Convert PDFs and export to Microsoft Word, Excel, and PowerPoint
# Redact to permanently remove sensitive visible information
# Compare two versions of a PDF to review all differences

# ****************************************************************************

import os
from datetime import datetime
from pypdf import PdfReader
from pypdf import PdfWriter
from tkinter import messagebox
from tkinter import filedialog


def split_pdfs():
    pdf_writer_front = PdfWriter()
    pdf_writer_back = PdfWriter()

    # Loop through files for PDFs with even pages
    count = 0  # Count for total files split
    for filename in os.listdir('..'):
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
    """Allows the user to select multiple files to merge, as well as what order to merge them in."""

    valid = False
    while not valid:  # 'not' checks for false boolean value
        file = filedialog.askopenfilenames(
            filetypes=[("PDF files", "*.pdf")],
            title="Please select files to merge:",
            initialdir=os.getcwd())

        if not file:
            return 1  # If file returns false the cancel button was pressed, so nothing and return to main menu

        if len(file) <= 1:  # More than 1 file must be chosen to merge
            messagebox.showerror(title="Error: Not enough files chosen",
                                 message="Error: You must choose more than 1 file to merge.")
        else:
            print('merge function here')


"""
    pdf_writer = PdfWriter()
    count = 0  # Count for total files merged
    for filename in os.listdir('..'):
        if filename.endswith('.pdf'):
            pdf_reader = PdfReader(filename)
            count = count + 1
            pdf_writer.append(fileobj=pdf_reader)

    if count <= 1:
        return tkinter.messagebox.showerror(title="Error: Not enough files",
                                    message="Error: Not enough PDF files to complete merge operation.")

    current_time = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

    output = open(current_time + "-merged_output.pdf", "wb")
    pdf_writer.write(output)
    pdf_writer.close()
    tkinter.messagebox.showinfo("PDF Merge Completed", f"{count} files merged.")
"""


