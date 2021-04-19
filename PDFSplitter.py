'''
PSEUDOCODE
    Navigate to location of PDF
    Select PDF
    for pages in pdf:
        Split PDF per page
        save with incremented number
'''

#import os and PyPDF2
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

#PDF splitter function
def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)

    #iterate through each page and split
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        #save page with new filename num+1
        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
        print('Created: {}'.format(output_filename))

#invoke pdf_splitter function
if __name__ == '__main__':
    path = str(input('Enter path to PDF: '))
    pdf_splitter(path)
