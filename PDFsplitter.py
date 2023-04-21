#!/usr/bin/env python3

import os
from pypdf import PdfWriter
from pypdf import PdfReader
from datetime import datetime


# todo:
# - docstrings
# - PEP8
# - create safeguards and checks
# - pythonic project and script structure
# -

def split_pdfs():
    # Create PDF writer objects to add pages to
    pdf_writer_front = PdfWriter()
    pdf_writer_back = PdfWriter()

    # Loop through files for PDFs with even pages
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            # Create PDF reader to handle files
            pdf_reader = PdfReader(filename)

            if len(pdf_reader.pages) % 2 == 0:
                pdf_writer_front.append(fileobj=pdf_reader, pages=(0, (int(len(pdf_reader.pages) / 2))))
                pdf_writer_back.append(fileobj=pdf_reader,
                                       pages=(int(len(pdf_reader.pages) / 2), int(len(pdf_reader.pages))))

    current_time = str(datetime.now())

    frontOutput = open(current_time+"FRONTOUTPUT.pdf", "wb")
    backOutput = open(current_time+"BACKOUTPUT.pdf", "wb")
    pdf_writer_front.write(frontOutput)
    pdf_writer_back.write(backOutput)

    pdf_writer_front.close()
    pdf_writer_back.close()


def main():
    split_pdfs()


if __name__ == '__main__':
    main()
