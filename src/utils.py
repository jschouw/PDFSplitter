#!/usr/bin/env python3

"""
    Functionality and logic of the program, including both GUI creation and PDF manipulation.
"""

# the intended audience for this project is an everyday office employee needing to manipulate
# PDF files in simple ways without having to pay for Adobe Acrobat. complement Acrobat free
# version, offering functionality that it does not, or that you normally would need to pay for.
# it will require a simple GUI for the layperson, but should also allow CLI use for the tech-inclined.
# this program is essentially an easier-to-use wrapper for pypdf


# [brainstorm]
# acrobat viewer is the free version, and it can basically only open PDF files.
# functionality brainstorming: merge, splice, split, metadata operations, extract text, extract images,
# encrypt/password, reduce file size
# Edit text and images, reorder, and delete pages in a PDF
# Convert PDFs and export to Microsoft Word, Excel, and PowerPoint
# Redact to permanently remove sensitive visible information
# Compare two versions of a PDF to review all differences

# GUI brainstorm:
# 1 main window with a logo and a series of buttons, each button opening the respective PDF process
# merge button will open a window that allows you to select multiple files to merge, then opens a 2nd dialog for confirmation of the order of documents
# split button will open a window that allows you to select just 1 file, and then a 2nd dialog for confirmation of the split location
# splice button will open a window that shows the PDF, and alongside it will be a text entry box for the page(s), with a 2nd dialog for confirmation that shows the new PDF
# metadata operations button will open a filechooser, then ask what operation to do, then confirm
# extracta text and extract images buttons will

# CLI brainstorm:
#

# program structure brainstorm:
#

# ****************************************************************************

import os
import tkinter
from datetime import datetime
from pypdf import PdfReader
from pypdf import PdfWriter
from tkinter import messagebox


def split_pdfs():
    """Splits PDFs in working directory.

    Splits all PDF files in half by page number and outputs two long PDF files
    of the merged halves.
    """
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
        return tkinter.messagebox.showerror(title="Error: No files", message="Error: No PDF files to split.")

    current_time = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    front_output = open(current_time + "-front-split-output.pdf", "wb")
    back_output = open(current_time + "-back-split-output.pdf", "wb")
    pdf_writer_front.write(front_output)
    pdf_writer_back.write(back_output)
    pdf_writer_front.close()
    pdf_writer_back.close()
    tkinter.messagebox.showinfo("PDF Split Completed", f"{count} file(s) split.")


def merge_pdfs():
    """Merges PDFs in working directory."""

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



