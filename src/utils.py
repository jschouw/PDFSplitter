#!/usr/bin/env python3

"""
    Functionality and logic of the program, including both GUI creation and PDF manipulation.
"""

# to-do: create output.write() function that automatically encodes strings (check extract_metadata function)

# [brainstorming:]
# functionality to-do: splice, metadata operations
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


def merge_pdfs():
    """Allows the user to select multiple files to merge, as well as what order to merge them in."""

    valid = False
    while not valid:  # 'not' checks for false boolean value
        file = filedialog.askopenfilenames(  # Open file choosing dialog window
            filetypes=[("PDF files", "*.pdf")],
            title="Please select files to merge:",
            initialdir=os.getcwd())

        if not file:  # If file returns false the cancel button was pressed, so nothing and return to main menu
            return 1

        if len(file) <= 1:  # More than 1 file must be chosen to merge
            messagebox.showerror(title="Error: Not enough files chosen",
                                 message="Error: You must choose more than 1 file to merge.")
        else:
            pdf_writer = PdfWriter()

            for filename in file:
                pdf_reader = PdfReader(filename)  # Read the PDF
                pdf_writer.append(fileobj=pdf_reader)  # Write the PDF to the Writer object by appending to end of file

            current_time = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))  # Get current time for unique filename
            output = open(current_time + "-merged_output.pdf", "wb")  # Open the file to write to
            pdf_writer.write(output)  # Write the PdfWriter object to the open file
            pdf_writer.close()

            valid = True  # For cleanup, but I'm not sure if it is even necessary with the return statement

            return messagebox.showinfo(title="Merge successful",
                                       message="Files merged successfully.")


def extract_text():
    """ Extracts the text from a PDF file and saves it to a text file. """

    valid = False
    while not valid:
        file = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")],
            title="Please select a file to extract text from:",
            initialdir=os.getcwd())

        if not file:  # If file returns false the cancel button was pressed, so nothing and return to main menu
            return 1
        else:
            pdf_reader = PdfReader(file)
            page = pdf_reader.pages[0]
            current_time = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))  # Get current time for unique filename
            filename = current_time + "-text_output.txt"
            output = open(filename, "wb")
            output.write(page.extract_text().encode())  # encode function converts string to bytes
            output.close()

            return messagebox.showinfo(title="Text extraction successful",
                                       message="Text extracted successfully and saved to:\n\n" +
                                       filename + ".")


def extract_images():
    """ Extracts the images from a PDF file and saves them to the program's directory. """

    """
        https://pypdf.readthedocs.io/en/stable/user/metadata.html
    """
    valid = False
    while not valid:
        file = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")],
            title="Please select a file to extract images from:",
            initialdir=os.getcwd())

        if not file:  # If file returns false the cancel button was pressed, so nothing and return to main menu
            return 1
        else:
            pdf_reader = PdfReader(file)
            page = pdf_reader.pages[0]
            count = 0
            for image_file_object in page.images:
                with open(str(count) + image_file_object.name, "wb") as fp:
                    fp.write(image_file_object.data)
                    count += 1
            if count == 0:
                return messagebox.showerror(title="No images in document",
                                            message="No images in the selected PDF document.")
            return messagebox.showinfo(title="Image extraction successful",
                                       message="Images extracted successfully and saved to file.")


def edit_metadata():
    """ Allows the user to edit the metadata of a PDF file. """
    valid = False
    while not valid:
        file = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")],
            title="Please select a file to edit:",
            initialdir=os.getcwd())

        if not file:  # If file returns false the cancel button was pressed, so nothing and return to main menu
            return 1
        else:
            pdf_reader = PdfReader(file)
            pdf_writer = PdfWriter(file)

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            metadata = pdf_reader.metadata
            pdf_writer.add_metadata(metadata)

            utc_time = "-05'00'"  # UTC time optional
            time = datetime.now().strftime(f"D\072%Y%m%d%H%M%S{utc_time}")



            for item in metadata:
                messagebox.askquestion(title=("Edit field: " + str(item)),
                                       message="Field value currently " + metadata.get(item),
                                       )

            pdf_writer.add_metadata(
                {
                    "/Author": "Martin",
                    "/Producer": "Libre Writer",
                    "/Title": "Title",
                    "/Subject": "Subject",
                    "/Keywords": "Keywords",
                    "/CreationDate": time,
                    "/ModDate": time,
                    "/Creator": "Creator",
                })

            with open("meta-pdf.pdf", "wb") as f:
                pdf_writer.write(f)

            return messagebox.showinfo(title="Metadata edit successful",
                                       message="Metadata successfully edited.")


def extract_metadata():
    """ Extracts the metadata of a PDF file and saves it to a text file. """

    valid = False
    while not valid:
        file = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")],
            title="Please select a file to extract metadata from:",
            initialdir=os.getcwd())

        if not file:  # If file returns false the cancel button was pressed, so nothing and return to main menu
            return 1
        else:
            pdf_reader = PdfReader(file)

            meta = pdf_reader.metadata

            current_time = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))  # Get current time for unique filename
            filename = current_time + "-metadata_output.txt"
            output = open(filename, "wb")

            output.write("******************************************************************".encode())
            output.write(str(filename).encode())
            output.write("******************************************************************".encode())
            output.write("\n\n".encode())
            output.write(("Metadata extracted from " + file.title() + "\n").encode())
            output.write(("# of metadata fields: " + str(meta.__len__()) + "\n\n").encode())
            output.write("****************************************\n".encode())
            output.write("[Raw Metadata Table:]\n\n".encode())
            output.write(str(meta).encode())
            output.write("\n\n****************************************".encode())
            output.write("\n\n\n\n[Formatted Metadata:]\n".encode())
            formatted_text = ""
            count = 1
            for item in meta:
                formatted_text = (formatted_text + "\n*******" +
                                  "\n[Metadata Field # " + str(count) + "]" +
                                  "\n[Field Name:] " + str(item) +
                                  "\n[Field Value:] " + meta.get(item) +
                                  "\n*******\n\n")
                count = count + 1

            output.write(formatted_text.encode())

            output.close()

            return messagebox.showinfo(title="Metadata extraction successful",
                                       message="Metadata extracted successfully and saved to:\n\n" +
                                       filename + ".")

