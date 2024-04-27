from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
from tkinter.ttk import *
from src.utils import *


def pdf_tools_gui():
    """Starts tkinter GUI loop for running pdf-tools scripts."""

    root = Tk()
    root.title('pdftools')
    frame = Frame(root, padding=5)  # Frame widget to fit in root window
    frame.grid()
    logo = PhotoImage(file='img/logo.png')
    Label(frame, image=logo).grid(column=0, row=0)
    Button(frame, text='Merge PDFs', command=merge_pdfs).grid(column=0, row=1)
    Button(frame, text='Extract text', command=extract_text).grid(column=0, row=3)
    Button(frame, text='Extract images', command=extract_images).grid(column=0, row=4)
    Button(frame, text='Extract metadata', command=extract_metadata).grid(column=0, row=5)
    Button(frame, text='Encrypt PDF', command=encrypt_pdf).grid(column=0, row=6)
    Button(frame, text='Decrypt PDF', command=decrypt_pdf).grid(column=0, row=7)
    Button(frame, text='Exit', command=root.destroy).grid(column=0, row=8)
    root.mainloop()


def merge_file_selection_window():
    return filedialog.askopenfilenames(
        filetypes=[('PDF files', '*.pdf')],
        title='Please select files to merge:',
        initialdir=os.getcwd()
    )


def merge_error_not_enough_files():
    return messagebox.showerror(title='Error: Not enough files chosen',
                                message='Error: You must choose more than 1 file to merge.')


def merge_filename_saveas_dialog():
    return filedialog.asksaveasfilename(
        initialfile='merged-output.pdf',
        initialdir=os.getcwd(),
        title='Please enter filename for merged output:',
        filetypes=[('PDF files', '*.pdf')]
    )


def save_successful_dialog(filename):
    return messagebox.showinfo(
        title='Save successful',
        message=f'{filename} successfully saved.'
    )


def extract_text_file_selection_dialog():
    return filedialog.askopenfilename(
            filetypes=[('PDF files', '*.pdf')],
            title='Please select a file to extract text from:',
            initialdir=os.getcwd())


def extract_text_filename_saveas_dialog():
    return filedialog.asksaveasfilename(
            filetypes=[('.txt files', '*.txt')],
            title='Please enter filename for text output:',
            initialdir=os.getcwd(),
            initialfile='text-output.txt'
    )


def extract_text_formatting_warning():
    return messagebox.showwarning(
                title='Formatting Warning',
                message='Please note that extracted text is likely to be poorly formatted.'
            )


def extract_images_file_selection_dialog():
    return filedialog.askopenfilename(
            filetypes=[('PDF files', '*.pdf')],
            title='Please select a file to extract ímages from:',
            initialdir=os.getcwd())


def extract_images_error_no_images():
    messagebox.showerror(title='No images in document',
                         message='No images in the selected PDF document.')


def extract_images_successful(extracted_images_count):
    messagebox.showinfo(title='Image extraction successful',
                        message=f'{extracted_images_count} images extracted and saved to file.')


def extract_metadata_file_selection_dialog():
    return filedialog.askopenfilename(
            filetypes=[('PDF files', '*.pdf')],
            title='Please select a file to extract metadata from:',
            initialdir=os.getcwd())


def extract_metadata_filename_saveas_dialog():
    return filedialog.asksaveasfilename(
            filetypes=[('.txt files', '*.txt')],
            title='Please enter filename for metadata output:',
            initialdir=os.getcwd(),
            initialfile='metadata-output.txt')


def encrypt_pdf_file_selection_dialog():
    return filedialog.askopenfilename(
            filetypes=[('PDF files', '*.pdf')],
            title='Please select a PDF to encrypt:',
            initialdir=os.getcwd())


def enter_encrypt_password_dialog():
    return simpledialog.askstring('Password Input',
                                  'Please input a password for the encrypted PDF:',
                                  initialvalue='(Will not be encrypted if entry left empty.)')


def encrypt_pdf_successful_dialog(encrypted_filename):
    return messagebox.showinfo(title='PDF encryption successful',
                        message=f'Encrypted PDF saved as {encrypted_filename}.')


def decrypt_pdf_file_selection_dialog():
    return filedialog.askopenfilename(
            filetypes=[('PDF files', '*.pdf')],
            title='Please select a file to decrypt:',
            initialdir=os.getcwd())


def enter_decrypt_password_dialog():
    return simpledialog.askstring('Password Input',
                                  'Please input a password to decrypt the PDF:')


def decrypt_pdf_successful_dialog(decrypted_filename):
    return messagebox.showinfo(title='PDF decryption successful',
                               message=f'Decrypted PDF saved as {decrypted_filename}.')


def decrypt_pdf_bad_password_error():
    return messagebox.showerror(title='Incorrect Password',
                                message='Password incorrect, try again.')


def decrypt_pdf_not_encrypted_error():
    messagebox.showerror(title='PDF is not encrypted',
                         message='You must choose an encrypted PDF to decrypt it.')

