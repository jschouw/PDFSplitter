"""
    Functionality and logic of the program.
"""

import os
import json
from pypdf import PdfReader
from pypdf import PdfWriter
from uuid import uuid4
import src.gui as gui


def merge_pdfs():
    """Allows the user to select multiple files to merge, as well as what order to merge them in."""

    while True:  # Loop to open a file dialog
        files = gui.merge_file_selection_window()

        if not files:  # If files returns false the cancel button was pressed, so do nothing and return to main menu
            return 0

        if len(files) < 2:  # If less than two files are selected, display error and return to file dialog
            gui.merge_error_not_enough_files()

        else:
            save_filename = gui.merge_filename_saveas_dialog()

            pdf_writer = PdfWriter()

            for filename in files:  # Loop through selected files
                pdf_reader = PdfReader(filename)
                pdf_writer.append(pdf_reader)  # Write the PDF to the Writer object by appending to end of file

            output = open(save_filename, 'wb')  # Open the file to write to
            pdf_writer.write(output)  # Write the PdfWriter object to the open file
            pdf_writer.close()

            return gui.save_successful_dialog(os.path.basename(save_filename))


def extract_text():
    """ Extracts the text from a PDF file and saves it to a text file. """

    while True:  # Loop to open a file dialog
        file = gui.extract_text_file_selection_dialog()

        if not file:  # If file returns false the cancel button was pressed, so do nothing and return to main menu
            return 0

        else:
            save_filename = gui.extract_text_filename_saveas_dialog()

            pdf_reader = PdfReader(file)
            output = open(save_filename, 'wb')

            for page in pdf_reader.pages:  # Loop through pages, extract text, write to open file
                output.write(page.extract_text(
                    extraction_mode='layout',  # Attempts to preserve layout in source PDF
                    layout_mode_space_vertically=False).encode()  # Encode function converts string to bytes
                             )

            output.close()
            gui.save_successful_dialog(os.path.basename(save_filename))

            return gui.extract_text_formatting_warning()


def extract_images():
    """ Extracts the images from a PDF file and saves them to the program's directory. """

    while True:  # Loop to open a file dialog
        file = gui.extract_images_file_selection_dialog()

        if not file:  # If file returns false the cancel button was pressed, so nothing and return to main menu
            return 0

        else:
            pdf_reader = PdfReader(file)
            count = 0  # Count number of images to later display an error if there are none in the PDF

            for page in pdf_reader.pages:  # Loop through all pages in PDF
                for image_file_object in page.images:  # Loop through all images on each page
                    # Open file to write, using UUID4 to create a unique filename
                    with open(f'{uuid4()} - {image_file_object.name}', 'wb') as image_output:
                        image_output.write(image_file_object.data)
                        count += 1

                if not count:
                    return gui.extract_images_error_no_images()

            return gui.extract_images_successful(count)


def extract_metadata():
    """ Extracts the metadata of a PDF file and saves it to a text file. """

    while True:  # Loop to open a file dialog
        file = gui.extract_metadata_file_selection_dialog()

        if not file:  # If file returns false the cancel button was pressed, so nothing and return to main menu
            return 0

        else:
            save_filename = gui.extract_metadata_filename_saveas_dialog()

            pdf_reader = PdfReader(file)
            meta = pdf_reader.metadata

            with open(save_filename, 'w') as output_file:
                json.dump(meta, output_file, indent=4)

            return gui.save_successful_dialog(os.path.basename(save_filename))


def encrypt_pdf():
    """ Encrypts a PDF file with a password. """

    while True:  # Loop to open a file dialog
        file = gui.encrypt_pdf_file_selection_dialog()

        if not file:  # If file returns false the cancel button was pressed, so nothing and return to main menu
            return 0

        else:
            while True:  # Start another loop, in case user leaves password field empty
                password = gui.enter_encrypt_password_dialog()

                if password:
                    pdf_reader = PdfReader(file)
                    pdf_writer = PdfWriter(clone_from=pdf_reader)

                    pdf_writer.encrypt(password, algorithm="AES-256")

                    save_file_name = f'{file} - encrypted - {uuid4()}.pdf'

                    with open(save_file_name, "wb") as f:
                        pdf_writer.write(f)

                    return gui.encrypt_pdf_successful_dialog(os.path.basename(save_file_name))
                else:
                    return 0


def decrypt_pdf():
    """ Decrypts an encrypted PDF file with a password. """

    while True:  # Loop to open a file dialog
        file = gui.decrypt_pdf_file_selection_dialog()

        if not file:  # If file returns false the cancel button was pressed, so nothing and return to main menu
            return 0

        else:
            while True:  # Start another loop, in case user leaves password field empty

                pdf_reader = PdfReader(file)

                if pdf_reader.is_encrypted:

                    password = gui.enter_decrypt_password_dialog()

                    if password:

                        if pdf_reader.decrypt(password):
                            pdf_writer = PdfWriter(clone_from=pdf_reader)

                            save_file_name = f'{file} - decrypted - {uuid4()}.pdf'

                            with open(save_file_name, "wb") as f:
                                pdf_writer.write(f)

                            return gui.decrypt_pdf_successful_dialog(os.path.basename(save_file_name))
                        else:
                            return gui.decrypt_pdf_bad_password_error()
                    else:
                        return 0
                else:
                    return gui.decrypt_pdf_not_encrypted_error()
